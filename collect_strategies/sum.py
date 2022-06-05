from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class SumStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        result, _ = self.get_sum(api_results)
        return result