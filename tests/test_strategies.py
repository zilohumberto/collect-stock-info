import unittest
from collect_strategies import (
    FactoryStrategy,
    CountStrategy,
    AverageStrategy,
)


class TestStrategies(unittest.TestCase):

    def test_count(self):
        self.assertEqual(CountStrategy().process([]), {})
        self.assertEqual(
            CountStrategy().process(
                [
                    {"stop_loss": 300},
                    {"stop_loss": 100},
                    {"stop_loss": 200}
                ]
            ),
            {"stop_loss": 600}
        )
        self.assertEqual(
            CountStrategy().process(
                [
                    {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                    {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                    {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
                ]
            ),
            {"deductible": 3200, "stop_loss": 33000, "oop_max": 17000}
        )

    def test_avg(self):
        self.assertEqual(AverageStrategy().process([]), {})
        self.assertEqual(
            AverageStrategy().process(
                [
                    {"stop_loss": 300},
                    {"stop_loss": 100},
                    {"stop_loss": 200}
                ]
            ),
            {"stop_loss": 200}
        )
        self.assertEqual(
            AverageStrategy().process(
                [
                    {"deductible": 1000, "stop_loss": 10000, "oop_max": 5000},
                    {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                    {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
                ]
            ),
            {"deductible": 1066, "stop_loss": 11000, "oop_max": 5666}
        )

    def test_factory(self):
        with self.assertRaises(NotImplementedError) as context:
            FactoryStrategy.choose_strategy("multiply")

        self.assertEqual(FactoryStrategy.choose_strategy(strategy="count"), CountStrategy)
        self.assertEqual(FactoryStrategy.choose_strategy(strategy="average"), AverageStrategy)
        self.assertEqual(FactoryStrategy.choose_strategy(), AverageStrategy)
        self.assertEqual(FactoryStrategy.choose_strategy(None), AverageStrategy)
