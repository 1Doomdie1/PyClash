from pyclash.utils.types.player import Player
from os                         import getenv
from unittest                   import TestCase
from pyclash                    import PlayersAPI
from dotenv                     import load_dotenv
from pyclash.utils.types.token  import VerifyToken


class test_PlayersAPI(TestCase):
    def setUp(self):
        load_dotenv()

        self.account_api_token = getenv("ACCOUNT_API_TOKEN")
        self.playerTag         = getenv("PLAYER_TAG")
        self.playersAPI        = PlayersAPI(getenv("API_KEY"))
    
    def test_get_player_info(self):
        resp = self.playersAPI.get_player_info(self.playerTag)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), Player)
        self.assertEqual(resp.body.tag, self.playerTag)

    def test_verify_player_token(self):
        resp = self.playersAPI.verify_player_token(self.playerTag, self.account_api_token)

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(type(resp.body), VerifyToken)
        self.assertEqual(resp.body.tag, self.playerTag)