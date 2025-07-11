from pyclash.utils.types.leagues import League 
from pydantic                    import BaseModel
from typing_extensions           import List, Optional, Dict
from pyclash.utils.types.common  import BadgeUrls, IconUrls, Label, Paging


class PlayerClan(BaseModel):
    tag:       str
    clanLevel: int
    name:      str
    badgeUrls: BadgeUrls

class League(BaseModel):
    name:     str
    id:       int
    iconUrls: IconUrls

class BuilderBaseLeague(BaseModel):
    name: str
    id:   int

class LegendLeagueTournamentSeasonResult(BaseModel):
    trophies: int
    id:       Optional[str] = None
    rank:     Optional[int] = None

class PlayerLegendStatistics(BaseModel):
    legendTrophies:            int
    bestSeason:                LegendLeagueTournamentSeasonResult
    currentSeason:             LegendLeagueTournamentSeasonResult
    bestBuilderBaseSeason:     Optional[LegendLeagueTournamentSeasonResult] = None
    previousBuilderBaseSeason: Optional[LegendLeagueTournamentSeasonResult] = None
    previousSeason:            Optional[LegendLeagueTournamentSeasonResult] = None

class PlayerItemLevel(BaseModel):
    level:              int
    name:               str
    maxLevel:           int
    village:            str
    equipment:          Optional[List[Dict]] = None

class PlayerAchievementProgress(BaseModel):
    stars:          int
    value:          int
    name:           str
    target:         int
    info:           str
    completionInfo: Optional[str] = None
    village:        str

class PlayerHouseElement(BaseModel):
    id:   int
    type: str

class PlayerHouse(BaseModel):
    elements: List[PlayerHouseElement]

class PalyerRankingClan(BaseModel):
    tag:       str
    name:      str
    badgeUrls: BadgeUrls

class PlayerRanking(BaseModel):
    clan:         Optional[PalyerRankingClan] = None
    league:       Optional[League] = None
    attackWins:   int
    defenseWins:  int
    tag:          str
    name:         str
    expLevel:     int
    rank:         int
    previousRank: Optional[int] = None
    trophies:     int

class PlayerRankings(BaseModel):
    items:  List[PlayerRanking]
    paging: Paging

class Player(BaseModel):
    clan:                     PlayerClan
    league:                   League
    builderBaseLeague:        BuilderBaseLeague
    role:                     str
    warPreference:            str
    attackWins:               int
    defenseWins:              int
    townHallLevel:            int
    townHallWeaponLevel:      int
    legendStatistics:         Optional[PlayerLegendStatistics] = None
    troops:                   List[PlayerItemLevel]
    heroes:                   List[PlayerItemLevel]
    heroEquipment:            List[PlayerItemLevel]
    spells:                   List[PlayerItemLevel]
    labels:                   List[Label]
    tag:                      str
    name:                     str
    expLevel:                 int
    trophies:                 int
    bestTrophies:             int
    donations:                int
    donationsReceived:        int
    builderHallLevel:         int
    builderBaseTrophies:      int
    bestBuilderBaseTrophies:  int
    warStars:                 int
    achievements:             List[PlayerAchievementProgress]
    clanCapitalContributions: int
    playerHouse:              PlayerHouse
