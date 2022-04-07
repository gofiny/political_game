from fastapi import Request
from fastapi.responses import JSONResponse

from utils.exceptions import DatabaseException


def database_error(request: Request, exc: DatabaseException):
    return JSONResponse(status_code=exc.code, content={"details": exc.message})
