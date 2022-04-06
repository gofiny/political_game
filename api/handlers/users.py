from uuid import UUID, uuid4

from api.schemas.users import NewUserRequest, UserResponse
from database.db import DBConnection
from game_core.users.models.user import User
from repositories.specific.users import UserPostgresRepo


async def create_new_user(
    new_user: NewUserRequest, db: DBConnection
) -> UserResponse:
    async with db:
        user = User(
            uid=uuid4(),
            service_id=new_user.service_id,
            nickname=new_user.nickname,
        )
        await UserPostgresRepo(db).add(user)
        await db.commit()

        return UserResponse(**vars(user))


async def get_user_by_uid(uid: UUID, db: DBConnection) -> UserResponse:
    async with db:
        user = await UserPostgresRepo(db).get(uid)
        return UserResponse(**vars(user))
