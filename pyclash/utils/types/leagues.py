from typing_extensions         import List
from pydantic                  import BaseModel
from pyclash.utils.types.other import Paging, IconUrls


class League(BaseModel):
    id:       int
    name:     str
    iconUrls: IconUrls

class Leagues(BaseModel):
    items:  List[League]
    paging: Paging

class LeagueSeason(BaseModel):
    id: str

class LeagueSeasons(BaseModel):
    items:  List[LeagueSeason]
    paging: Paging

class WarAndCapitalAndBuilderBaseLeague(BaseModel):
    name: str
    id:   int

class WarAndCapitalAndBuilderBaseLeagues(BaseModel):
    items:  List[WarAndCapitalAndBuilderBaseLeague]
    paging: Paging