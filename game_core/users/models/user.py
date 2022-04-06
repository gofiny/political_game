from datetime import datetime, timezone
from uuid import UUID


class User:
    def __init__(
        self,
        uid: UUID,
        service_id: str,
        nickname: str,
        created_at: datetime = datetime.now(tz=timezone.utc),
        updated_at: datetime = datetime.now(tz=timezone.utc),
        is_active: bool = True,
    ):
        self.uid = uid
        self.service_id = service_id
        self.nickname = nickname
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active

    @classmethod
    def from_kwargs(cls, **kwargs) -> "User":
        return User(**kwargs)
