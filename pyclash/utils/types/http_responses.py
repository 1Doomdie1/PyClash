from pyclash.utils.types.player import Player
from pyclash.utils.types.token import *
from pydantic import BaseModel
from typing_extensions import Optional, Dict, Union


class ClientError(BaseModel):
    reason:  str
    message: Optional[str]  = None
    type:    Optional[str]  = None
    detail:  Optional[Dict] = None

class Response(BaseModel):
    body:        Union[Player, VerifyToken, ClientError]
    status_code: int