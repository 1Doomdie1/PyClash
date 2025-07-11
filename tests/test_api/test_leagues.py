from os                          import getenv
from unittest                    import TestCase
from pyclash                     import LeaguesAPI
from dotenv                      import load_dotenv
from pyclash.utils.types.player  import PlayerRankings
from pyclash.utils.types.leagues import WarAndCapitalAndBuilderBaseLeagues, WarAndCapitalAndBuilderBaseLeague, Leagues, League, LeagueSeasons


class test_LeaguesAPI(TestCase):
    def setUp(self):
        load_dotenv()

        self.league_id         = getenv("LEAGUE_ID")
        self.war_league_id     = getenv("WAR_LEAGUE_ID")
        self.capital_league_id = getenv("CAPITAL_LEAGUE_ID")
        self.leagueAPI         = LeaguesAPI(getenv("API_KEY"))
    
    def test_capital_leagues(self):
        resp = self.leagueAPI.capital_leagues()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), WarAndCapitalAndBuilderBaseLeagues)
    
    def test_capital_league(self):
        resp = self.leagueAPI.capital_league(leagueId = self.capital_league_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), WarAndCapitalAndBuilderBaseLeague)

    def test_leagues(self):
        resp = self.leagueAPI.leagues()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Leagues)

    def test_league(self):
        resp = self.leagueAPI.league(leagueId = self.league_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), League)
    
    def test_league_seasons(self):
        resp = self.leagueAPI.league_seasons(leagueId = self.league_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), LeagueSeasons)
    
    def test_league_season(self):
        resp = self.leagueAPI.league_season(leagueId = self.league_id, seasonId = "2025-06")

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), PlayerRankings)
    
    
    def test_builder_base_leagues(self):
        resp = self.leagueAPI.builder_base_leagues()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), WarAndCapitalAndBuilderBaseLeagues)
    
    def test_builder_base_league(self):
        resp = self.leagueAPI.builder_base_leagues()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), WarAndCapitalAndBuilderBaseLeagues)
    
    def test_war_leagues(self):
        resp = self.leagueAPI.war_leagues()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), WarAndCapitalAndBuilderBaseLeagues)
    
    def test_war_league(self):
        resp = self.leagueAPI.war_league(leagueId = self.war_league_id)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), WarAndCapitalAndBuilderBaseLeague)