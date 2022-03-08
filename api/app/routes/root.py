from logging import getLogger
from os import getpid
from socket import gethostname
from typing import Final

from app import settings
from app.models.push_report import PushReport
from app.models.push_type import PushType
from app.models.sent_message import SentMessage
from app.models.sent_message_type import SentMessageType
from app.schemas.root_response import RootResponse
from fastapi import APIRouter, WebSocket
from fastapi.encoders import jsonable_encoder
from starlette.websockets import WebSocketDisconnect

PATH: Final = ""
ROUTER: Final = APIRouter()
LOGGER: Final = getLogger(__file__)


ws_connections = []


@ROUTER.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json(
        jsonable_encoder(
            PushReport(
                push_type=PushType.CONNECTED_TO,
                host=gethostname(),
                pid=getpid(),
                initiated_by=SentMessageType.CONNECT_INITIATED,
            )
        )
    )
    ws_connections.append(websocket)
    try:
        while True:
            received_message = SentMessage(**await websocket.receive_json())
            push_report = PushReport(
                push_type=PushType.NOTIFIED_BY,
                host=gethostname(),
                pid=getpid(),
                initiated_by=received_message.sent_message_type,
            )
            for connection in ws_connections:
                await connection.send_json(jsonable_encoder(push_report))
    except WebSocketDisconnect:
        ws_connections.remove(websocket)


@ROUTER.get("/", response_model=RootResponse)
async def root():
    return RootResponse(api_name=settings.NAME)
