from typing import Any, MutableMapping, Sequence, Tuple


class BaseStrategy:

    def process(self, api_results: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        raise NotImplementedError()
    
    def get_sum(self, results: Sequence[MutableMapping[str, Any]]) -> Tuple[
        MutableMapping[str, Any], MutableMapping[str, Any]
    ]:
        sum_dict = {}
        cnt_dict = {}
        for api_result in results:
            for key, value in api_result.items():
                if key not in sum_dict:
                    sum_dict[key] = 0
                if key not in cnt_dict:
                    cnt_dict[key] = 0

                sum_dict[key] += value
                cnt_dict[key] += 1
        return sum_dict, cnt_dict

    def get_avg(
            self,
            cnt_dict: MutableMapping[str, Any],
            results: MutableMapping[str, Any]
    ) -> MutableMapping[str, Any]:
        return {key: int(value / cnt_dict[key]) for key, value in results.items()}
