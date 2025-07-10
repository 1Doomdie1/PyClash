from pydantic import BaseModel
from typing_extensions import Literal, List, Optional, Dict


class PlayerClan(BaseModel):
    tag:       str
    clanLevel: int
    name:      str
    badgeUrls: dict

class League(BaseModel):
    name:     str
    id:       int
    iconUrls: dict

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
    village:            Literal["home", "builderBase", "clanCapital"]
    equipment:          Optional[List[Dict]] = None

class Label(BaseModel):
    name:     str
    id:       int
    iconUrls: dict

class PlayerAchievementProgress(BaseModel):
    stars:          int
    value:          int
    name:           str
    target:         int
    info:           str
    completionInfo: Optional[str] = None
    village:        Literal["home", "builderBase", "clanCapital"]

class PlayerHouseElement(BaseModel):
    id:   int
    type: Literal["ground", "roof", "foot", "decoration", "walls"]

class PlayerHouse(BaseModel):
    elements: List[PlayerHouseElement]

class Player(BaseModel):
    clan:                     PlayerClan
    league:                   League
    builderBaseLeague:        BuilderBaseLeague
    role:                     Literal["not_member", "member", "leader", "admin", "coLeader"]
    warPreference:            Literal["in", "out"]
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
