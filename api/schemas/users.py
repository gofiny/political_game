from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class NewUserRequest(BaseModel):
    service_id: str = Field(..., max_length=50)
    nickname: str = Field(..., max_length=50)


class UserResponse(BaseModel):
    uid: UUID
    service_id: str
    nickname: str
    created_at: datetime
    updated_at: datetime
    is_active: bool


class UserPatchResponse(BaseModel):
    nickname: Optional[str] = Field(..., max_length=50)
    is_active: bool
