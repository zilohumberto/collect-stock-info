from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class AverageStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        cnt_dict = {}
        if len(api_results) == 0:
            return cnt_dict

        for api_result in api_results:
            for key, value in api_result.items():
                if key not in cnt_dict:
                    cnt_dict[key] = 0

                cnt_dict[key] += value

        return {key: int(value / len(api_results)) for key, value in cnt_dict.items()}
