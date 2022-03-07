from pydantic import BaseModel


class RootResponse(BaseModel):
    api_name: str
