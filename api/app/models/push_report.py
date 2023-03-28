from time import time
from typing import Optional

from app.models.push_type import PushType
from app.models.sent_message_type import SentMessageType
from pydantic import BaseModel


class PushReport(BaseModel):
    push_type: PushType
    host: str
    pid: int
    initiated_by: SentMessageType
    report_time: Optional[float] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.report_time = round(time() * 1000)
