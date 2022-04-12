from pydantic import BaseSettings


class Config(BaseSettings):
    LOGGING_CONFIG: str


config = Config()
