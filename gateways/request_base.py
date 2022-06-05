from requests import get


class GatewayRequestBase:
    url = None

    def __init__(self, url: str):
        self.url = url

    async def do_get(self, params):
        """
            perform the request raise error if status code is not 200
        """
        response = get(
            url=self.url,
            params=params,
            timeout=5,
        )

        if response.status_code == 200:
            return response.json()

        raise ValueError(response.text)
