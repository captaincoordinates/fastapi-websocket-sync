from time import time
from typing import Optional

from app.models.push_type import PushType
from pydantic import BaseModel


class PushReport(BaseModel):

    push_type: PushType
    host: str
    pid: int
    report_time: Optional[float] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.report_time = time()
