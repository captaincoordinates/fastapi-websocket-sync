from enum import Enum


class PushType(str, Enum):
    CONNECTED_TO = "connected_to"
    NOTIFIED_BY = "notified_by"
