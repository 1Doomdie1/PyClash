from pyclash.utils.types.common import Paging
from pydantic                   import BaseModel
from typing_extensions          import List, Optional

class Location(BaseModel):
    localizedName: Optional[str] = None
    id:            int
    name:          str
    isCountry:     bool
    countryCode:   Optional[str] = None

class Locations(BaseModel):
    items:  List[Location]
    paging: Paging
