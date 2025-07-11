from pyclash.utils.types.token   import *
from pyclash.utils.types.common  import GoldPass
from pydantic                    import BaseModel
from typing_extensions           import Optional, Dict, Union
from pyclash.utils.types.player  import Player, PlayerRankings
from pyclash.utils.types.clans   import ClanList, Clan, ClanMemberList, ClanCapitalRaidSeasonList, ClanWar, ClanWarLog #, ClanWarLeagueGroup
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
                #ClanWarLeagueGroup
                WarAndCapitalAndBuilderBaseLeagues, Leagues, League,
                LeagueSeasons, PlayerRankings, WarAndCapitalAndBuilderBaseLeague,
                GoldPass
            ]
    # body: PlayerRankings
    status_code: int