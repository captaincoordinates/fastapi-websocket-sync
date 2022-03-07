from app import settings
from fastapi import status


def test_root_handler(test_app):
    response = test_app.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["api_name"] == settings.NAME
