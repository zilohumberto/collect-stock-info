from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class AverageStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        sum_dict = self.get_sum(api_results)
        return self.get_avg(num_of_elements=len(api_results), results=sum_dict)
