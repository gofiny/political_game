import logging
from uuid import UUID

from fastapi import APIRouter, Depends

from api.handlers.users import (
    create_new_user,
    get_all_users,
    get_user_by_uid,
    update_user_by_uid,
)
from api.schemas.users import NewUserRequest, UserPatchResponse, UserResponse
from api.utils import get_db

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Users"])


@router.post("/users", response_model=UserResponse)
async def create_user(new_user: NewUserRequest, db=Depends(get_db)):
    user = await create_new_user(new_user, db)
    return user


@router.get("/users/{uid}", response_model=UserResponse)
async def get_user(uid: UUID, db=Depends(get_db)):
    user = await get_user_by_uid(uid, db)
    return user


@router.get("/users", response_model=list[UserResponse])
async def get_users(db=Depends(get_db)):
    users = await get_all_users(db)
    return users


@router.patch("/users/{uid}", response_model=UserResponse)
async def update_user(uid: UUID, update: UserPatchResponse, db=Depends(get_db)):
    user = await update_user_by_uid(uid, update, db)
    return user
