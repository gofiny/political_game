from pydantic import BaseSettings


class DBConfig(BaseSettings):
    DB_DSN: str
    DB_POOL_MAX_SIZE: int
    DB_POOL_MIN_SIZE: int


config = DBConfig()
