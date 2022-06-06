from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class MinStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        min_dict = {}
        for api_result in api_results:
            for key, value in api_result.items():
                if key not in min_dict:
                    min_dict[key] = api_result[key]
                else:
                    min_dict[key] = min(min_dict[key], api_result[key])

        return min_dict
