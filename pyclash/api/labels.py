from pyclash.utils.types.common         import Labels
from pyclash.client                            import Client
from typing_extensions                  import Optional
from pyclash.utils.types.http_responses import Response

class LabelsAPI(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.endpoint = "labels"

    def players(
        self,
        limit:  int = 100,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/players",
            params = {key: value for key, value in locals().items() if value is not None and key is not "self"}
        )

        return Response(body = Labels(**req.json()), status_code = req.status_code)
    
    def clans(
        self,
        limit:  int = 100,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/clans",
            params = {key: value for key, value in locals().items() if value is not None and key is not "self"}
        )

        return Response(body = Labels(**req.json()), status_code = req.status_code)