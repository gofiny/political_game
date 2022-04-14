from uuid import UUID, uuid4

from api.schemas.states import (
    NewStateRequest,
    StatePatchResponse,
    StateResponse,
)
from database.db import DBConnection
from game_core.states.models.states import State
from repositories.specific.states import StatePostgresRepo


async def create_new_state(
    new_state: NewStateRequest, db: DBConnection
) -> StateResponse:
    async with db:
        state = State(
            uid=uuid4(),
            name=new_state.name,
            leader_uid=new_state.leader_uid,
        )
        await StatePostgresRepo(db).add(state)
        await db.commit()

        return StateResponse(**vars(state))


async def get_state_by_uid(uid: UUID, db: DBConnection) -> StateResponse:
    async with db:
        state = await StatePostgresRepo(db).get(uid)
        return StateResponse(**vars(state))


async def get_all_states(db: DBConnection) -> list[StateResponse]:
    async with db:
        states = await StatePostgresRepo(db).get_all()
        return [StateResponse(**vars(state)) for state in states]


async def update_state_by_uid(
    uid: UUID, updating_fields: StatePatchResponse, db: DBConnection
) -> StateResponse:
    async with db:
        state = await StatePostgresRepo(db).update(
            uid, updating_fields.dict(exclude_unset=True)
        )

        return StateResponse(**vars(state))
