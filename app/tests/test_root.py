from fastapi import status

from app import settings


def test_root_handler(test_app):
    response = test_app.get("/")
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["api_name"] == settings.NAME
