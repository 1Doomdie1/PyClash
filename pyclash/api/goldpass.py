from pyclash                            import Client
from pyclash.utils.types.http_responses import Response

class GoldPassAPI(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.endpoint = "goldpass"
    
    def info(
        self
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/seasons/current"
        )

        return Response(body = req.json(), status_code = req.status_code)