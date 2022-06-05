from typing import Optional
from collect_strategies.sum import SumStrategy
from collect_strategies.average import AverageStrategy
from collect_strategies.standar_deviation import StandardDeviationStrategy


class FactoryStrategy:
    strategies = {
        "average": AverageStrategy(),
        "sum": SumStrategy(),
        "std": StandardDeviationStrategy(),
    }

    @classmethod
    def choose_strategy(cls, strategy: Optional[str] = "average"):
        strategy = strategy or "average"
        if strategy in cls.strategies:
            return cls.strategies[strategy]

        raise NotImplementedError(strategy)
