from pyclash.utils.types.token   import *
from pydantic                    import BaseModel
from pyclash.utils.types.common  import GoldPass, Labels
from typing_extensions           import Optional, Dict, Union
from pyclash.utils.types.player  import Player, PlayerRankings
from pyclash.utils.types.clans   import ClanList, Clan, ClanMemberList, ClanCapitalRaidSeasonList, ClanWar, ClanWarLog
from pyclash.utils.types.leagues import Leagues, League, LeagueSeasons, WarAndCapitalAndBuilderBaseLeague, WarAndCapitalAndBuilderBaseLeagues


class ClientError(BaseModel):
    reason:  str
    message: Optional[str]  = None
    type:    Optional[str]  = None
    detail:  Optional[Dict] = None

class Response(BaseModel):
    body: Union[ClientError, Player, VerifyToken, 
                ClanList, Clan, ClanMemberList, 
                ClanCapitalRaidSeasonList, ClanWar, ClanWarLog,
                WarAndCapitalAndBuilderBaseLeagues, Leagues, League,
                LeagueSeasons, PlayerRankings, WarAndCapitalAndBuilderBaseLeague,
                GoldPass, Labels
            ]
    status_code: int