from pyclash.client                     import Client
from typing_extensions                  import Optional
from pyclash.utils.types.http_responses import Response
from pyclash.utils.types.clans          import ClanCapitalRankings

class LocationAPI(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.endpoint = "locations"
    
    def list(
        self,
        limit:  int           = 30,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}",
            params = {key: value for key, value in locals().items() if value is not None and key != "self"}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def get(
        self,
        locationId: str
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{locationId}"
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def capitals_rankings(
        self,
        locationId: str,
        limit:      int           = 30,
        after:      Optional[str] = None,
        before:     Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{locationId}/rankings/capitals",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "locationId")}
        )

        return Response(body = ClanCapitalRankings(**req.json()), status_code = req.status_code)
    
    def clans_rankings(
        self,
        locationId: str,
        limit:      int           = 30,
        after:      Optional[str] = None,
        before:     Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{locationId}/rankings/clans",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "locationId")}
        )

        return Response(body = req.json(), status_code = req.status_code)

    def players_rankings(
        self,
        locationId: str,
        limit:      int           = 30,
        after:      Optional[str] = None,
        before:     Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{locationId}/rankings/players",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "locationId")}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def players_builder_base_rankings(
        self,
        locationId: str,
        limit:      int           = 30,
        after:      Optional[str] = None,
        before:     Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{locationId}/rankings/players-builder-base",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "locationId")}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def clans_builder_base_rankings(
        self,
        locationId: str,
        limit:      int           = 30,
        after:      Optional[str] = None,
        before:     Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{locationId}/rankings/clans-builder-base",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "locationId")}
        )

        return Response(body = req.json(), status_code = req.status_code)