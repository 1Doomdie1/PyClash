from pyclash.utils.types.token    import *
from pydantic                     import BaseModel
from pyclash.utils.types.common   import GoldPass, Labels
from pyclash.utils.types.location import Locations, Location
from typing_extensions            import Optional, Dict, Union
from pyclash.utils.types.player   import (
    Player, PlayerRankings, 
    PlayerBuilderBaseRankings
)
from pyclash.utils.types.leagues  import (
    Leagues, League, LeagueSeasons, 
    WarAndCapitalAndBuilderBaseLeague, 
    WarAndCapitalAndBuilderBaseLeagues
)
from pyclash.utils.types.clans    import (
    ClanList, Clan, ClanMemberList, 
    ClanCapitalRaidSeasonList, ClanWar, 
    ClanWarLog, ClanCapitalRankings, 
    ClanRankings, ClanBuilderBaseRankings
)


class ClientError(BaseModel):
    reason:  Optional[str]  = None
    message: Optional[str]  = None
    type:    Optional[str]  = None
    detail:  Optional[Dict] = None

class Response(BaseModel):
    body: Union[ClientError, Player, VerifyToken, 
                ClanList, Clan, ClanMemberList, 
                ClanCapitalRaidSeasonList, ClanWar, ClanWarLog,
                WarAndCapitalAndBuilderBaseLeagues, Leagues, League,
                LeagueSeasons, PlayerRankings, WarAndCapitalAndBuilderBaseLeague,
                GoldPass, Labels, Locations, Location, ClanCapitalRankings,
                ClanRankings, PlayerBuilderBaseRankings, ClanBuilderBaseRankings
            ]
    status_code: int