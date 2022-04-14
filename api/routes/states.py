import logging
from uuid import UUID

from fastapi import APIRouter, Depends

from api.handlers.states import (
    create_new_state,
    get_all_states,
    get_state_by_uid,
    update_state_by_uid,
)
from api.schemas.states import (
    NewStateRequest,
    StatePatchResponse,
    StateResponse,
)
from api.utils import get_db

logger = logging.getLogger(__name__)

router = APIRouter(tags=["States"])


@router.post("/states", response_model=StateResponse)
async def create_state(new_state: NewStateRequest, db=Depends(get_db)):
    state = await create_new_state(new_state, db)
    return state


@router.get("/states/{uid}", response_model=StateResponse)
async def get_state(uid: UUID, db=Depends(get_db)):
    state = await get_state_by_uid(uid, db)
    return state


@router.get("/states", response_model=list[StateResponse])
async def get_states(db=Depends(get_db)):
    states = await get_all_states(db)
    return states


@router.patch("/states/{uid}", response_model=StateResponse)
async def update_state(
    uid: UUID, update: StatePatchResponse, db=Depends(get_db)
):
    state = await update_state_by_uid(uid, update, db)
    return state
