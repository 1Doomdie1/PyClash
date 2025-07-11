from os                           import getenv
from unittest                     import TestCase
from pyclash                      import LocationAPI
from dotenv                       import load_dotenv
from pyclash.utils.types.location import Locations, Location
from pyclash.utils.types.player   import PlayerRankings, PlayerBuilderBaseRankings
from pyclash.utils.types.clans    import ClanCapitalRankings, ClanRankings, ClanBuilderBaseRankings


class test_LocationAPI(TestCase):
    def setUp(self):
        load_dotenv()

        self.location_id = getenv("LOCATION_ID")
        self.locationAPI = LocationAPI(getenv("API_KEY"))
    
    def test_list(self):
        resp = self.locationAPI.list()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Locations)
    
    def test_get(self):
        resp = self.locationAPI.get(locationId = self.location_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Location)
    
    def test_capitals_rankings(self):
        resp = self.locationAPI.capitals_rankings(locationId = self.location_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanCapitalRankings)
    
    def test_clans_rankings(self):
        resp = self.locationAPI.clans_rankings(locationId = self.location_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanRankings)
    
    def test_players_rankings(self):
        resp = self.locationAPI.players_rankings(locationId = self.location_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), PlayerRankings)
    
    def test_players_builder_base_rankings(self):
        resp = self.locationAPI.players_builder_base_rankings(locationId = self.location_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), PlayerBuilderBaseRankings)
    
    def test_clans_builder_base_rankings(self):
        resp = self.locationAPI.clans_builder_base_rankings(locationId = self.location_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanBuilderBaseRankings)