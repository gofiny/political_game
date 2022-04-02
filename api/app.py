import logging

from fastapi import FastAPI

from .config import config
from .routes import health_check

logger = logging.getLogger(__name__)


app = FastAPI(title=config.APP_NAME, version=config.VERSION, debug=config.DEBUG)

app.include_router(health_check.router)
