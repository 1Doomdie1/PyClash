from pyclash.utils.types.common import Labels
from os                         import getenv
from unittest                   import TestCase
from pyclash                    import LabelsAPI
from dotenv                     import load_dotenv


class test_LabelsAPI(TestCase):
    def setUp(self):
        load_dotenv()

        self.labelsAPI = LabelsAPI(getenv("API_KEY"))
    
    def test_players(self):
        resp = self.labelsAPI.players()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Labels)
    
    def test_clans(self):
        resp = self.labelsAPI.clans()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Labels)