from abc import ABC, abstractmethod

from asyncpg import Connection, Pool, create_pool
from asyncpg.transaction import Transaction

from .config import config


class AbstractConnection(ABC):
    async def commit(self):
        await self._commit()

    async def rollback(self):
        await self._rollback()

    @abstractmethod
    async def _commit(self):
        raise NotImplementedError

    @abstractmethod
    async def _rollback(self):
        raise NotImplementedError

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        raise NotImplementedError


class AbstractDB(ABC):
    async def start(self):
        await self._start()

    async def stop(self):
        await self._stop()

    async def get_connection(self):
        return await self._get_connection()

    async def release_connection(self, connection):
        await self._release_connection(connection)

    @abstractmethod
    async def _start(self):
        raise NotImplementedError

    @abstractmethod
    async def _stop(self):
        raise NotImplementedError

    @abstractmethod
    async def _get_connection(self):
        raise NotImplementedError

    @abstractmethod
    async def _release_connection(self, connection):
        raise NotImplementedError


class DB(AbstractDB):
    def __init__(self):
        self._pool: Pool = create_pool(
            dsn=config.DB_DSN,
            min_size=config.DB_POOL_MIN_SIZE,
            max_size=config.DB_POOL_MAX_SIZE,
        )

    async def _start(self):
        await self._pool

    async def _stop(self):
        await self._pool.close()

    async def _get_connection(self):
        return await self._pool.acquire()

    async def _release_connection(self, connection: Connection):
        await self._pool.release(connection)


class DBConnection(AbstractConnection):
    def __init__(self, db: DB):
        self._db = db
        self.connection: Connection | None = None
        self._transaction: Transaction | None = None
        self._is_committed: bool = False

    async def _commit(self):
        if self._transaction is not None:
            self._is_committed = True
            await self._transaction.commit()

    async def _rollback(self):
        if self._transaction is not None and self._is_committed is False:
            await self._transaction.rollback()

    async def _start_transaction(self):
        self._transaction = self.connection.transaction()
        await self._transaction.start()

    async def __aenter__(self):
        self.connection: Connection = await self._db.get_connection()
        await self._start_transaction()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self._rollback()
        await self._db.release_connection(self.connection)
