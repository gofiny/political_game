from httpx import Response


async def test_check_alive(client):
    response: Response = await client.get("/check_alive")

    assert response.status_code == 200
    assert response.json() == {"ok": True}
