from pyclash.utils.types.common import GoldPass
from os                         import getenv
from unittest                   import TestCase
from pyclash                    import GoldPassAPI
from dotenv                     import load_dotenv


class test_GoldPassAPI(TestCase):
    def setUp(self):
        load_dotenv()

        self.golpassAPI = GoldPassAPI(getenv("API_KEY"))
    
    def test_info(self):
        resp = self.golpassAPI.info()

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), GoldPass)