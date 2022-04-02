import logging

from fastapi import APIRouter

from api.schemas.common import Ok

logger = logging.getLogger(__name__)

router = APIRouter(tags=["Health check"])


@router.get("/check_alive", response_model=Ok)
async def check_alive():
    return Ok(ok=True)
