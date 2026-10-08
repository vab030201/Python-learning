from fastapi import APIRouter, Depends, HTTPException, Request, status

from app.schemas.policy_schema import PolicyCreate, PolicyResponse, PolicyUpdate
from app.services.policy_services import PolicyService

router = APIRouter(prefix="/api/policies", tags=["Policies"])


def get_policy_service(request: Request) -> PolicyService:
    return request.app.state.policy_service


@router.get("/", response_model=list[PolicyResponse])
async def get_all_policies(service: PolicyService = Depends(get_policy_service)):
    return await service.get_all_policies()


@router.get("/{policy_id}", response_model=PolicyResponse)
async def get_policy(policy_id: int, service: PolicyService = Depends(get_policy_service)):
    policy = await service.get_policy(policy_id)
    if policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return policy


@router.post("/", response_model=PolicyResponse, status_code=status.HTTP_201_CREATED)
async def create_policy(policy: PolicyCreate, service: PolicyService = Depends(get_policy_service)):
    try:
        return await service.create_policy(policy.model_dump())
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.put("/{policy_id}", response_model=PolicyResponse)
async def update_policy(
    policy_id: int,
    policy: PolicyUpdate,
    service: PolicyService = Depends(get_policy_service),
):
    try:
        updated = await service.update_policy(policy_id, policy.model_dump())
        if updated is None:
            raise HTTPException(status_code=404, detail="Policy not found")
        return updated
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.delete("/{policy_id}")
async def delete_policy(policy_id: int, service: PolicyService = Depends(get_policy_service)):
    deleted = await service.delete_policy(policy_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Policy not found")
    return {"message": "Policy deleted successfully", "policy_id": policy_id}
