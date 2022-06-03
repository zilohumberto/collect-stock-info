from requests import get


class GatewayRequestBase:
    url = None

    def __init__(self, url: str):
        self.url = url

    async def do_get(self, params):
        # TODO TIMEOUT RETRIES AND ASYNC
        response = get(
            url=self.url,
            params=params,
        )

        if response.status_code == 200:
            return response.json()

        raise ValueError(response.text)
