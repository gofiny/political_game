from uuid import UUID

from asyncpg import Connection

from database.db import DBConnection
from game_core.states.models.states import State
from repositories.abstract.states import StateAbstractRepo
from utils.exceptions import DatabaseException
from utils.sql import build_args


class StatePostgresRepo(StateAbstractRepo):
    def __init__(self, connection: DBConnection):
        self._connection: Connection = connection.connection

    async def _add(self, user: State):
        await self._connection.execute(
            "INSERT INTO states "
            "(uid, name, leader)"
            "VALUES ($1, $2, $3)",
            user.uid,
            user.name,
            user.leader_uid,
        )

    async def _get(self, uid: UUID) -> State:
        state_record = await self._connection.fetchrow(
            "SELECT * FROM states WHERE uid = $1", uid
        )

        if state_record is None:
            raise DatabaseException(f"State with {uid=} not found", code=404)

        return State.from_kwargs(**dict(state_record))

    async def _get_all(self) -> list[None | State]:
        states_record = await self._connection.fetch("SELECT * FROM states")
        return [State.from_kwargs(**dict(state)) for state in states_record]

    async def _update(self, uid: UUID, updating_fields: dict) -> State:
        k, v = tuple(updating_fields.keys()), tuple(updating_fields.values())
        args = build_args(k)
        state_record = await self._connection.fetchrow(
            f"UPDATE states SET {args} "
            f"WHERE uid=${len(updating_fields) + 1} RETURNING *",
            *v,
            uid,
        )
        return State.from_kwargs(**dict(state_record))
