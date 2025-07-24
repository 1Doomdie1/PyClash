from pyclash.client                     import Client
from typing_extensions                  import Optional
from pyclash.utils.types.http_responses import Response

class LeaguesAPI(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.endpoint = "leagues"
    
    def capital_leagues(
        self,
        limit:  int = 30,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response: 
        req = self._http_request(
            "GET",
            f"capital{self.endpoint}",
            params = {key: value for key, value in locals().items() if value is not None and key is not "self"}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def capital_league(
        self,
        leagueId: int
    ) -> Response: 
        req = self._http_request(
            "GET",
            f"capital{self.endpoint}/{leagueId}",
        )

        return Response(body = req.json(), status_code = req.status_code)
 
    def leagues(
        self,
        limit:  int = 30,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}",
            params = {key: value for key, value in locals().items() if value is not None and key is not "self"}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def league(
        self,
        leagueId: str
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{leagueId}"
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def league_seasons(
        self,
        leagueId: int,
        limit:  int = 100,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{leagueId}/seasons",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "leagueId")}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def league_season(
        self,
        leagueId: str,
        seasonId: str,
        limit:    int = 100,
        after:    Optional[str] = None,
        before:   Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{leagueId}/seasons/{seasonId}",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "leagueId", "seasonId")}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def builder_base_leagues(
        self,
        limit:  int = 30,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"builderbase{self.endpoint}",
            params = {key: value for key, value in locals().items() if value is not None and key is not "self"}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def builder_base_league(
        self,
        leagueId: str
    ) -> Response:
        req = self._http_request(
            "GET",
            f"builderbase{self.endpoint}/{leagueId}"
        )

        return Response(body = req.json(), status_code = req.status_code)

    def war_leagues(
        self,
        limit:  int = 100,
        after:  Optional[str] = None,
        before: Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"war{self.endpoint}",
            params = {key: value for key, value in locals().items() if value is not None and key is not "self"}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def war_league(
        self,
        leagueId: str,
    ) -> Response:
        req = self._http_request(
            "GET",
            f"war{self.endpoint}/{leagueId}"
        )
        body = req.json()
        body.pop("iconUrls", None)
        
        return Response(body = body, status_code = req.status_code)
