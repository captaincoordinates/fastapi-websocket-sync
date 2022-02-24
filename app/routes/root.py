from logging import getLogger
from os import getpid
from socket import gethostname
from typing import Final

from fastapi import APIRouter, WebSocket
from fastapi.encoders import jsonable_encoder
from starlette.websockets import WebSocketDisconnect

from app import settings
from app.models.push_report import PushReport
from app.models.push_type import PushType
from app.schemas.root_response import RootResponse

PATH: Final = ""
ROUTER: Final = APIRouter()
LOGGER: Final = getLogger(__file__)


ws_connections = []


@ROUTER.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(
        jsonable_encoder(
            PushReport(push_type=PushType.CONNECTED_TO, host=gethostname(), pid=getpid())
        )
    )
    ws_connections.append(websocket)
    try:
        while True:
            await websocket.receive_text()
            for connection in ws_connections:
                await connection.send_json(
                    jsonable_encoder(
                        PushReport(
                            push_type=PushType.NOTIFIED_BY,
                            host=gethostname(),
                            pid=getpid(),
                        )
                    )
                )
    except WebSocketDisconnect:
        ws_connections.remove(websocket)


@ROUTER.get("/", response_model=RootResponse)
async def root():
    return RootResponse(api_name=settings.NAME)
