from abc import ABC, abstractmethod
from uuid import UUID

from game_core.users.models.user import User


class UserAbstractRepo(ABC):
    async def add(self, user: User):
        return await self._add(user)

    async def get(self, uid: UUID) -> User:
        return await self._get(uid)

    async def get_all(self) -> list[None | User]:
        return await self._get_all()

    async def update(self, uid: UUID, updating_fields: dict) -> User:
        return await self._update(uid, updating_fields)

    @abstractmethod
    async def _add(self, user: User):
        raise NotImplementedError

    @abstractmethod
    async def _get(self, uid: UUID) -> User:
        raise NotImplementedError

    @abstractmethod
    async def _get_all(self) -> list[None | User]:
        raise NotImplementedError

    @abstractmethod
    async def _update(self, uid: UUID, updating_fields: dict) -> User:
        raise NotImplementedError
