import asyncio

import pytest
from starlette.testclient import TestClient

from app.main import app


@pytest.fixture(scope="session")
def event_loop(request):
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def test_app():
    with TestClient(app) as client:
        yield client
