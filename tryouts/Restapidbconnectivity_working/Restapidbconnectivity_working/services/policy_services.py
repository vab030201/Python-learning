from app.repository.policy_repositories import PolicyRepository


class PolicyService:
    def __init__(self, repository: PolicyRepository):
        self.repository = repository

    async def get_all_policies(self):
        return await self.repository.get_all()

    async def get_policy(self, policy_id: int):
        return await self.repository.get_by_id(policy_id)

    async def create_policy(self, policy_data: dict):
        self._validate_premium(policy_data)
        return await self.repository.create(policy_data)

    async def update_policy(self, policy_id: int, policy_data: dict):
        if await self.repository.get_by_id(policy_id) is None:
            return None
        self._validate_premium(policy_data)
        return await self.repository.update(policy_id, policy_data)

    async def delete_policy(self, policy_id: int):
        return await self.repository.delete(policy_id)

    @staticmethod
    def _validate_premium(policy_data: dict):
        if policy_data["premium"] < 500:
            raise ValueError("Minimum premium must be 500")
