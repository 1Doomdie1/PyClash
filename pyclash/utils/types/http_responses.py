from pyclash.utils.types.token  import *
from pyclash.utils.types.player import Player
from pydantic                   import BaseModel
from typing_extensions          import Optional, Dict, Union
from pyclash.utils.types.clans  import ClanList, Clan, ClanMemberList, ClanCapitalRaidSeasonList, ClanWar, ClanWarLog #, ClanWarLeagueGroup


class ClientError(BaseModel):
    reason:  str
    message: Optional[str]  = None
    type:    Optional[str]  = None
    detail:  Optional[Dict] = None

class Response(BaseModel):
    body: Union[ClientError, Player, VerifyToken, 
                ClanList, Clan, ClanMemberList, 
                ClanCapitalRaidSeasonList, ClanWar, ClanWarLog
                #ClanWarLeagueGroup
            ]
    status_code: int