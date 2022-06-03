from typing import Sequence, MutableMapping, Any
from gateways.collect_data import CollectData
from collect_strategies.factory import FactoryStrategy
from settings import API_ONE, API_TWO, API_THREE


class CollectService:
    sources = []

    def __init__(self):
        self.sources.append(CollectData(url=API_ONE))
        self.sources.append(CollectData(url=API_TWO))
        self.sources.append(CollectData(url=API_THREE))

    async def _collect(self, member_id: str) -> Sequence[MutableMapping[Any]]:
        responses = []
        for source in self.sources:
            r = await source.process(member_id=member_id)
            print(f"Getting data from {source.url} -> {r}")
            responses.append(r)

        return responses

    async def collect(self, member_id: str, strategy: str = None) -> MutableMapping[Any]:
        api_results = await self._collect(member_id=member_id)
        strategy = FactoryStrategy.choose_strategy(strategy=strategy)
        return strategy.process(api_results=api_results)
