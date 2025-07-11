from urllib.parse                       import quote
from pyclash                            import Client
from pyclash.utils.types.http_responses import Response
from typing_extensions                  import Optional, List
from json import dumps

class ClansAPI(Client):
    def __init__(self, apiKey):
        super().__init__(apiKey)
        self.endpoint = "clans"
    
    def list(
        self,
        name:          Optional[str]       = None,
        warFrequency:  Optional[str]       = None,
        locationId:    Optional[int]       = None,
        minMembers:    Optional[int]       = None,
        maxMembers:    Optional[int]       = None,
        minClanPoints: Optional[int]       = None,
        minClanLevel:  Optional[int]       = None,
        limit:         Optional[int]       = 10,
        after:         Optional[str]       = None,
        before:        Optional[str]       = None,
        labelIds:      Optional[List[str]] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}",
            params = {key: value for key, value in locals().items() if value is not None and key != "self"}
        )

        return Response(body = req.json(), status_code = req.status_code)

    def get(
        self,
        clanTag: str
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{quote(clanTag)}"
        )
        return Response(body = req.json(), status_code = req.status_code)
    
    def members(
        self,
        clanTag: str,
        limit:   Optional[int] = None,
        after:   Optional[str] = None,
        before:  Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{quote(clanTag)}/members",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "clanTag")}
        )

        return Response(body = req.json(), status_code = req.status_code)
    
    def capital_raid_seasons(
        self,
        clanTag: str,
        limit:   Optional[int] = None,
        after:   Optional[str] = None,
        before:  Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{quote(clanTag)}/capitalraidseasons",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "clanTag")}
        )
        return Response(body = req.json(), status_code = req.status_code)

    def current_war(
        self,
        clanTag: str
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{quote(clanTag)}/currentwar"
        )
        return Response(body = req.json(), status_code = req.status_code)

    def war_log(
        self,
        clanTag: str,
        limit:   Optional[int] = None,
        after:   Optional[str] = None,
        before:  Optional[str] = None
    ) -> Response:
        req = self._http_request(
            "GET",
            f"{self.endpoint}/{quote(clanTag)}/warlog",
            params = {key: value for key, value in locals().items() if value is not None and key not in ("self", "clanTag")}
        )
        return Response(body = req.json(), status_code = req.status_code)
