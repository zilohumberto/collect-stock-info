from typing import Any, MutableMapping


class BaseStrategy:

    def process(self, api_results: MutableMapping[str, Any]) -> MutableMapping[str, Any]:
        raise NotImplementedError()
