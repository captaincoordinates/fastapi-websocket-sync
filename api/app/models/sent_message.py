from app.models.sent_message_type import SentMessageType
from pydantic import BaseModel


class SentMessage(BaseModel):
    sent_message_type: SentMessageType
