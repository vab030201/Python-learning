from pydantic import BaseModel, Field


class PolicyCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=5, max_length=255)
    maturity: str = Field(..., min_length=1, max_length=50)
    premium: float = Field(..., gt=0)


class PolicyUpdate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    description: str = Field(..., min_length=5, max_length=255)
    maturity: str = Field(..., min_length=1, max_length=50)
    premium: float = Field(..., gt=0)


class PolicyResponse(PolicyCreate):
    id: int
