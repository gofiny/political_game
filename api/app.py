import logging

from fastapi import FastAPI, Request

from database.db import DB, DBConnection

from .config import config
from .routes import health_check, users

logger = logging.getLogger(__name__)


app = FastAPI(title=config.APP_NAME, version=config.VERSION, debug=config.DEBUG)


async def on_startup():
    pool = DB()
    app.state.db = pool
    await pool.start()


async def on_shutdown():
    await app.state.db.stop()


async def db_session_middleware(request: Request, call_next):
    request.state.connection = DBConnection(app.state.db)
    return await call_next(request)


def prepare_app():
    app.add_event_handler("startup", on_startup)
    app.add_event_handler("shutdown", on_shutdown)

    app.middleware("http")(db_session_middleware)

    app.include_router(health_check.router)
    app.include_router(users.router)

    return app
