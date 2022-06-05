from math import sqrt
from typing import Any, Sequence, MutableMapping
from collect_strategies.base_strategy import BaseStrategy


class StandardDeviationStrategy(BaseStrategy):

    def process(self, api_results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        sum_dict, cnt_dict = self.get_sum(api_results)
        avg_dict = self.get_avg(cnt_dict=cnt_dict, results=sum_dict)
        std_dict = {}
        for key in sum_dict.keys():
            values = []
            for result in api_results:
                if key not in result:
                    continue
                values.append(pow(abs(result[key] - avg_dict[key]), 2))

            std_dict[key] = round(sqrt(sum(values) / cnt_dict[key]), 4)
        return std_dict
