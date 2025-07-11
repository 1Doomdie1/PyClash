from pyclash.utils.types.location import Location 
from pydantic                     import BaseModel
from typing_extensions            import List, Optional
from pyclash.utils.types.common   import Label, BadgeUrls, Paging
from pyclash.utils.types.player   import League, BuilderBaseLeague, PlayerHouse


class WarLeague(BaseModel):
    name: str
    id:   int

class CapitalLeague(BaseModel):
    name: str
    id:   int

class ClanMember(BaseModel):
    league:              League
    builderBaseLeague:   BuilderBaseLeague
    tag:                 str
    name:                str
    role:                str
    townHallLevel:       int
    expLevel:            int
    clanRank:            int
    previousClanRank:    int
    donations:           int
    donationsReceived:   int
    trophies:            int
    builderBaseTrophies: int
    playerHouse:         Optional[PlayerHouse] = None

class Language(BaseModel):
    name:         str
    id:           int
    languageCode: str

class ClanDistrictData(BaseModel):
    name:              str
    id:                int
    districtHallLevel: int


class ClanCapital(BaseModel):
    capitalHallLevel: int
    districts:        List[ClanDistrictData]

class Clan(BaseModel):
    warLeague:                   WarLeague
    capitalLeague:               CapitalLeague
    memberList:                  Optional[List[ClanMember]] = None
    tag:                         str
    warLosses:                   Optional[int]          = None
    clanPoints:                  int
    clanLevel:                   int
    warWinStreak:                int
    warWins:                     int
    warTies:                     Optional[int]          = None
    chatLanguage:                Optional[Language]     = None
    clanBuilderBasePoints:       int
    clanCapitalPoints:           int
    requiredTrophies:            int
    requiredBuilderBaseTrophies: int
    requiredTownhallLevel:       int
    isFamilyFriendly:            bool
    isWarLogPublic:              bool
    warFrequency:                str
    labels:                      List[Label]
    name:                        str
    location:                    Optional[Location]     = None
    type:                        str
    members:                     int
    description:                 Optional[str]          = None
    clanCapital:                 Optional[ClanCapital]  = None
    badgeUrls:                   BadgeUrls

class ClanList(BaseModel):
    items:  List[Clan]
    paging: Paging

class ClanMemberList(BaseModel):
    items:  List[ClanMember]
    paging: Paging

class ClanCapitalRaidSeasonClanInfo(BaseModel):
    tag:       str
    name:      str
    level:     int
    badgeUrls: BadgeUrls

class ClanCapitalRaidSeasonAttacker(BaseModel):
    tag:  str
    name: str

class ClanCapitalRaidSeasonAttack(BaseModel):
    attacker:           ClanCapitalRaidSeasonAttacker
    destructionPercent: int
    stars:              int

class ClanCapitalRaidSeasonDistrict(BaseModel):
    stars:              int
    name:               str
    id:                 int
    destructionPercent: int
    attackCount:        int
    totalLooted:        int
    attacks:            Optional[List[ClanCapitalRaidSeasonAttack]] = None
    districtHallLevel:  int

class ClanCapitalRaidSeasonAttackLog(BaseModel):
    defender:           ClanCapitalRaidSeasonClanInfo
    attackCount:        int
    districtCount:      int
    districtsDestroyed: int
    districts:          List[ClanCapitalRaidSeasonDistrict]

class ClanCapitalRaidSeasonDefenseLog(BaseModel):
    attacker: ClanCapitalRaidSeasonClanInfo
    attackCount:        int
    districtCount:      int
    districtsDestroyed: int
    districts:          List[ClanCapitalRaidSeasonDistrict]

class ClanCapitalRaidSeasonMember(BaseModel):
    tag:                    str
    name:                   str
    attacks:                int
    attackLimit:            int
    bonusAttackLimit:       int
    capitalResourcesLooted:	int

class ClanCapitalRaidSeason(BaseModel):
    attackLog:               List[ClanCapitalRaidSeasonAttackLog]
    defenseLog:              List[ClanCapitalRaidSeasonDefenseLog]
    state:                   str
    startTime:               str
    endTime:                 str
    capitalTotalLoot:        int
    raidsCompleted:          int
    totalAttacks:            int
    enemyDistrictsDestroyed: int
    offensiveReward:         int
    defensiveReward:         int
    members:                 Optional[List[ClanCapitalRaidSeasonMember]] = None

class ClanCapitalRaidSeasonList(BaseModel):
    items:  List[ClanCapitalRaidSeason]
    paging: Paging

class ClanWarAttack(BaseModel):
    order:                 int
    attackerTag:           str
    defenderTag:           str
    stars:                 int
    destructionPercentage: int
    duration:              int

class ClanWarMember(BaseModel):
    tag:                str
    name:               str
    mapPosition:        int
    townhallLevel:      int
    opponentAttacks:    int
    bestOpponentAttack: ClanWarAttack
    attacks:            List[ClanWarAttack]

class WarClan(BaseModel):
    destructionPercentage: float
    tag:                   Optional[str]                 = None
    name:                  Optional[str]                 = None
    badgeUrls:             BadgeUrls
    clanLevel:             int
    attacks:               Optional[int]                 = None
    stars:                 int
    expEarned:             Optional[int]                 = None
    members:               Optional[List[ClanWarMember]] = None

class ClanWar(BaseModel):
    clan:                 WarClan
    opponent:             WarClan
    teamSize:             Optional[int] = None
    attacksPerMember:     Optional[int] = None
    battleModifier:       Optional[str] = None
    startTime:            Optional[str] = None
    state:                str
    endTime:              Optional[str] = None
    preparationStartTime: Optional[str] = None

class ClanWarLogEntry(BaseModel):
    clan:             WarClan
    teamSize:         int
    attacksPerMember: Optional[int] = None
    battleModifier:   str
    opponent:         WarClan
    endTime:          str
    result:           Optional[str]

class ClanWarLog(BaseModel):
    items:  List[ClanWarLogEntry]
    paging: Paging

class ClanCapitalRanking(BaseModel):
    clanPoints:        Optional[int] = None
    clanCapitalPoints: int

class ClanCapitalRankings(BaseModel):
    items:  List[ClanCapitalRanking]
    paging: Paging

class ClanRanking(BaseModel):
    clanLevel:    int
    clanPoints:   int
    location:     Location
    members:      int
    tag:          str
    name:         str
    rank:         int
    previousRank: int
    badgeUrls:    BadgeUrls

class ClanRankings(BaseModel):
    items:  List[ClanRanking]
    paging: Paging

class ClanBuilderBaseRanking(BaseModel):
    clanBuilderBasePoints: int
    clanPoints:            Optional[int] = None

class ClanBuilderBaseRankings(BaseModel):
    items:  List[ClanBuilderBaseRanking]
    paging: Paging