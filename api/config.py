from pydantic import BaseConfig


class ApiConfig(BaseConfig):
    APP_NAME: str = "PoliticalGameApi"
    APP_HOST: str = "0.0.0.0"
    APP_PORT: str = "8000"
    VERSION: str = "0.0.1"
    DEBUG: bool = True


config = ApiConfig()
