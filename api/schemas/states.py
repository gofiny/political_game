from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class NewStateRequest(BaseModel):
    name: str = Field(..., max_length=50)
    leader_uid: UUID


class StateResponse(BaseModel):
    uid: UUID
    name: str = Field(..., max_length=50)
    leader_uid: UUID
    created_at: datetime
    updated_at: datetime
    is_active: bool


class StatePatchResponse(BaseModel):
    name: Optional[str] = Field(..., max_length=50)
    leader_uid: UUID
    is_active: bool
