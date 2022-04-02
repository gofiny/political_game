import pytest
from httpx import AsyncClient


@pytest.fixture
async def client():
    from api.app import app

    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client
