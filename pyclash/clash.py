from pyclash.client import Client
from pyclash.api    import (
    PlayersAPI, ClansAPI, 
    LabelsAPI, LeaguesAPI, 
    GoldPassAPI, LocationAPI
)


class Clash(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.clans     = ClansAPI(apiKey)
        self.labels    = LabelsAPI(apiKey)
        self.players   = PlayersAPI(apiKey)
        self.leagues   = LeaguesAPI(apiKey)
        self.goldpass  = GoldPassAPI(apiKey)
        self.locations = LocationAPI(apiKey)