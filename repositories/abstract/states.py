from abc import ABC, abstractmethod
from uuid import UUID

from game_core.states.models.states import State


class StateAbstractRepo(ABC):
    async def add(self, state: State):
        return await self._add(state)

    async def get(self, uid: UUID) -> State:
        return await self._get(uid)

    async def get_all(self) -> list[None | State]:
        return await self._get_all()

    async def update(self, uid: UUID, updating_fields: dict) -> State:
        return await self._update(uid, updating_fields)

    @abstractmethod
    async def _add(self, user: State):
        raise NotImplementedError

    @abstractmethod
    async def _get(self, uid: UUID) -> State:
        raise NotImplementedError

    @abstractmethod
    async def _get_all(self) -> list[None | State]:
        raise NotImplementedError

    @abstractmethod
    async def _update(self, uid: UUID, updating_fields: dict) -> State:
        raise NotImplementedError
