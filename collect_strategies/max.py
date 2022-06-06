from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class MaxStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        max_dict = {}
        for api_result in api_results:
            for key, value in api_result.items():
                if key not in max_dict:
                    max_dict[key] = 0

                max_dict[key] = max(max_dict[key], api_result[key])

        return max_dict
