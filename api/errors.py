import logging

from fastapi import Request
from fastapi.responses import JSONResponse

from utils.exceptions import DatabaseException

logger = logging.getLogger(__name__)


def database_error(request: Request, exc: DatabaseException):
    logger.error("database exception occur", exc_info=True)
    return JSONResponse(status_code=exc.code, content={"details": exc.message})
