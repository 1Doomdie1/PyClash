from pydantic import BaseModel


class VerifyToken(BaseModel):
    tag:    str
    token:  str
    status: str