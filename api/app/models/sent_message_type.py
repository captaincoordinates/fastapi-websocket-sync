from enum import Enum


class SentMessageType(str, Enum):
    USER_INITIATED = "user-initiated"
    CONNECT_INITIATED = "connect-initiated"
