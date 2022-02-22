from logging import getLogger
from typing import Final

from fastapi import APIRouter

from app import settings
from app.schemas.root_response import RootResponse

PATH: Final = ""
ROUTER: Final = APIRouter()
LOGGER: Final = getLogger(__file__)


@ROUTER.get("/", response_model=RootResponse)
async def root():
    return RootResponse(api_name=settings.NAME)
