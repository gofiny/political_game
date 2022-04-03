from abc import ABC, abstractmethod
from uuid import UUID

from game_core.users.models.user import User


class UserAbstractRepo(ABC):
    async def add(self, user: User):
        return await self._add(user)

    async def get(self, uuid: UUID) -> User:
        return await self._get(uuid)

    @abstractmethod
    async def _add(self, user: User):
        raise NotImplementedError

    @abstractmethod
    async def _get(self, uuid: UUID) -> User:
        raise NotImplementedError
