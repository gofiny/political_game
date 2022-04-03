from uuid import UUID

from asyncpg import Connection

from database.db import DBConnection
from game_core.users.models.user import User
from repositories.abstract.users import UserAbstractRepo
from repositories.exceptions import DatabaseException


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

    async def _get(self, uuid: UUID) -> User:
        user_record = await self._connection.fetchrow(
            "SELECT * FROM users WHERE uid = $1", uuid
        )

        if user_record is None:
            raise DatabaseException(f"User with {uuid=} not found")

        return User.from_kwargs(**dict(user_record))
