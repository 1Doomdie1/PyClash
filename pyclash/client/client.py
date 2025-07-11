from requests import Response, request 

class Client:
    verify_ssl: bool = True

    def __init__(self, apiKey: str) -> None:
        self.apiKey = apiKey

    def _http_request(
            self, 
            method:      str,
            endpoint:    str,
            api_version: str = "v1",
            **kwargs
        ) -> Response:
        url = f"https://api.clashofclans.com/{api_version}/{endpoint}"
        headers = {**kwargs.pop("headers", {}), "Authorization": f"Bearer {self.apiKey}"}
        
        return request(method, url, headers=headers, verify=Client.verify_ssl, **kwargs)