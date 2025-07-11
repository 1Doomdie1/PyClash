from typing_extensions import Optional
from pydantic          import BaseModel


class BadgeUrls(BaseModel):
    small:  str
    large:  str
    medium: str

class IconUrls(BaseModel):
    small:  str
    medium: Optional[str] = None
    tiny:   Optional[str] = None

class Label(BaseModel):
    name:     str
    id:       int
    iconUrls: dict

class Cursors(BaseModel):
    after: Optional[str] = None

class Paging(BaseModel):
    cursors: Cursors

class GoldPass(BaseModel):
    startTime: str
    endTime:   str
