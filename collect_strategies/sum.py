from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class SumStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        cnt_dict = {}
        for api_result in api_results:
            for key, value in api_result.items():
                if key not in cnt_dict:
                    cnt_dict[key] = 0

                cnt_dict[key] += value

        return cnt_dict
