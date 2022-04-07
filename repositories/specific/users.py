from uuid import UUID

from asyncpg import Connection

from database.db import DBConnection
from game_core.users.models.user import User
from repositories.abstract.users import UserAbstractRepo
from utils.exceptions import DatabaseException
from utils.sql import build_args


class UserPostgresRepo(UserAbstractRepo):
    def __init__(self, connection: DBConnection):
        self._connection: Connection = connection.connection

    async def _add(self, user: User):
        await self._connection.execute(
            "INSERT INTO users "
            "(uid, service_id, nickname)"
            "VALUES ($1, $2, $3)",
            user.uid,
            user.service_id,
            user.nickname,
        )

    async def _get(self, uid: UUID) -> User:
        user_record = await self._connection.fetchrow(
            "SELECT * FROM users WHERE uid = $1", uid
        )

        if user_record is None:
            raise DatabaseException(f"User with {uid=} not found", code=404)

        return User.from_kwargs(**dict(user_record))

    async def _get_all(self) -> list[None | User]:
        users_record = await self._connection.fetch("SELECT * FROM users")
        return [User.from_kwargs(**dict(user)) for user in users_record]

    async def _update(self, uid: UUID, updating_fields: dict) -> User:
        k, v = tuple(updating_fields.keys()), tuple(updating_fields.values())
        args = build_args(k)
        user_record = await self._connection.fetchrow(
            f"UPDATE users SET {args} "
            f"WHERE uid=${len(updating_fields) + 1} RETURNING *",
            *v,
            uid,
        )
        return User.from_kwargs(**dict(user_record))
