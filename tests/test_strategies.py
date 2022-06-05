import unittest
from collect_strategies import (
    FactoryStrategy,
    SumStrategy,
    AverageStrategy,
)


class TestStrategies(unittest.TestCase):

    def test_count(self):
        self.assertEqual(SumStrategy().process([]), {})
        self.assertEqual(
            SumStrategy().process(
                [
                    {"stop_loss": 300},
                    {"stop_loss": 100},
                    {"stop_loss": 200}
                ]
            ),
            {"stop_loss": 600}
        )
        self.assertEqual(
            SumStrategy().process(
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
        self.assertEqual(
            AverageStrategy().process(
                [
                    {"deductible": 1000, "stop_loss": 10000, },
                    {"deductible": 1200, "stop_loss": 13000, "oop_max": 6000},
                    {"deductible": 1000, "stop_loss": 10000, "oop_max": 6000},
                ]
            ),
            {"deductible": 1066, "stop_loss": 11000, "oop_max": 6000}
        )

    def test_factory(self):
        with self.assertRaises(NotImplementedError) as context:
            FactoryStrategy.choose_strategy("multiply")

        self.assertTrue(isinstance(FactoryStrategy.choose_strategy(strategy="sum"), SumStrategy))
        self.assertTrue(isinstance(FactoryStrategy.choose_strategy(strategy="average"), AverageStrategy))
        self.assertTrue(isinstance(FactoryStrategy.choose_strategy(), AverageStrategy))
        self.assertTrue(isinstance(FactoryStrategy.choose_strategy(None), AverageStrategy))
