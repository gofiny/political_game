from datetime import datetime, timezone
from uuid import UUID


class State:
    def __init__(
        self,
        uid: UUID,
        name: str,
        leader_uid: UUID,
        created_at: datetime = datetime.now(tz=timezone.utc),
        updated_at: datetime = datetime.now(tz=timezone.utc),
        is_active: bool = True,
    ):
        self.uid = uid
        self.name = name
        self.leader_uid = leader_uid
        self.created_at = created_at
        self.updated_at = updated_at
        self.is_active = is_active

    @classmethod
    def from_kwargs(cls, **kwargs) -> "State":
        return State(**kwargs)
