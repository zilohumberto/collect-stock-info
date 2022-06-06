from gateways.request_base import GatewayRequestBase


class CollectDataRequest(GatewayRequestBase):
    def __init__(self, url: str):
        super(CollectDataRequest, self).__init__(url=url)

    async def process(self, member_id: str):
        return await self.do_get(dict(member_id=member_id))
