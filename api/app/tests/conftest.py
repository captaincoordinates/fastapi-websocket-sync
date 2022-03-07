import asyncio

import pytest
from app.main import app
from starlette.testclient import TestClient


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def test_app():
    with TestClient(app) as client:
        yield client
