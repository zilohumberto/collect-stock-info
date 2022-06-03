from typing import Optional
from collect_strategies.count import CountStrategy
from collect_strategies.average import AverageStrategy


class FactoryStrategy:
    strategies = {
        "average": AverageStrategy,
        "count": CountStrategy,
    }

    @classmethod
    def choose_strategy(cls, strategy: Optional[str] = "average"):
        strategy = strategy or "average"
        if strategy in cls.strategies:
            return cls.strategies[strategy]

        raise NotImplementedError(strategy)
