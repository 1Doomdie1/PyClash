from os                         import getenv
from unittest                   import TestCase
from pyclash                    import ClansAPI
from dotenv                     import load_dotenv
from pyclash.utils.types.clans  import (
    ClanList, Clan, ClanMemberList, 
    ClanCapitalRaidSeasonList, 
    ClanWar, ClanWarLog
) 

class test_ClansAPI(TestCase):
    def setUp(self):
        load_dotenv()

        self.clanTag  = getenv("CLAN_TAG")
        self.clansAPI = ClansAPI(getenv("API_KEY"))
    
    def test_list(self):
        resp = self.clansAPI.list(name="test")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.body.items), 10)
        self.assertEqual(type(resp.body), ClanList)
    
    def test_get(self):
        resp = self.clansAPI.get(clanTag = self.clanTag)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Clan)

    def test_members(self):
        resp = self.clansAPI.members(clanTag = self.clanTag)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanMemberList)
    
    def test_capital_raid_seasons(self):
        resp = self.clansAPI.capital_raid_seasons(clanTag = self.clanTag)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanCapitalRaidSeasonList)
    
    def test_current_war(self):
        resp = self.clansAPI.current_war(clanTag = self.clanTag)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanWar)

    def test_war_log(self):
        resp = self.clansAPI.war_log(clanTag = self.clanTag)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), ClanWarLog)