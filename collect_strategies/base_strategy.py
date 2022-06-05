from typing import Any, MutableMapping, Sequence


class BaseStrategy:

    def process(self, api_results: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        raise NotImplementedError()
    
    def get_sum(self, results: Sequence[MutableMapping[str, Any]]) -> MutableMapping[str, Any]:
        sum_dict = {}
        for api_result in results:
            for key, value in api_result.items():
                if key not in sum_dict:
                    sum_dict[key] = 0

                sum_dict[key] += value
        
        return sum_dict

    def get_avg(self, num_of_elements: int, results: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        return {key: int(value / num_of_elements) for key, value in results.items()}
