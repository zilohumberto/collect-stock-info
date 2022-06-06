from typing import Sequence, MutableMapping, Any
from gateways.collect_data import CollectDataRequest
from collect_strategies.factory import FactoryStrategy
from settings import API_ONE, API_TWO, API_THREE


class CollectService:
    sources = []

    def __init__(self):
        self.sources.append(CollectDataRequest(url=API_ONE))
        self.sources.append(CollectDataRequest(url=API_TWO))
        self.sources.append(CollectDataRequest(url=API_THREE))

    async def _collect(self, member_id: str) -> Sequence[MutableMapping[str, Any]]:
        """
            iterate over 'sources' and collect each information by member_id independent
        """
        responses = []
        for source in self.sources:
            r = await source.process(member_id=member_id)
            print(f"Getting data from {source.url} -> {r}")
            responses.append(r)

        return responses

    async def collect(
        self, member_id: str, strategy: str = None
    ) -> MutableMapping[str, Any]:
        """
            collect info from member id from different apis
            choose the strategy and run it to process the information given!
        """
        api_results = await self._collect(member_id=member_id)
        strategy = FactoryStrategy.choose_strategy(strategy=strategy)
        return strategy.process(api_results=api_results)
