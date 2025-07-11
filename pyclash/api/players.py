from urllib.parse                       import quote
from pyclash.client                     import Client
from pyclash.utils.types.http_responses import Response

class PlayersAPI(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.endpoint = "players"

    def get_player_info(
        self,
        playerTag: str 
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{quote(playerTag)}"
        )

        return Response(body = req.json(), status_code = req.status_code)

    def verify_player_token(
        self,
        playerTag: str,
        token:     str
    ) -> Response:
        
        req =  self._http_request(
            "POST",
            f"{self.endpoint}/{quote(playerTag)}/verifytoken",
            json = {"token": token}
        )

        return Response(body = req.json(), status_code = req.status_code)