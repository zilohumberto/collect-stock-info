from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class SumStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        return self.get_sum(api_results)
