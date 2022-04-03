import logging
from uuid import UUID

from fastapi import APIRouter, Depends

from api.handlers.users import create_new_user, get_user_by_uid
from api.schemas.users import NewUserRequest, UserResponse
from api.utils import get_db

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Users"])


@router.post("/users", response_model=UserResponse)
async def create_user(new_user: NewUserRequest, db=Depends(get_db)):
    user: UserResponse = await create_new_user(new_user, db)
    return user


@router.get("/users/{uid}", response_model=UserResponse)
async def get_user(uid: UUID, db=Depends(get_db)):
    user: UserResponse = await get_user_by_uid(uid, db)
    return user
