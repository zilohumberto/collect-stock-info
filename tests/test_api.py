from tests.test_base import TestBase
from settings import API_ONE, API_TWO, API_THREE
from gateways.collect_data import CollectDataRequest
from collect_service import CollectService
from collect_strategies import FactoryStrategy


class TestApi(TestBase):
    apis = []

    def setUp(self) -> None:
        self.apis.append(CollectDataRequest(API_ONE))
        self.apis.append(CollectDataRequest(API_TWO))
        self.apis.append(CollectDataRequest(API_THREE))
        self.collect_service = CollectService()

    def test_endpoint(self):
        result = self.synchronize_async_helper(self.collect_service.collect(member_id="3"))
        self.assertEqual(type(result), dict), "result of api should be a dict"

    def test_strategy(self):
        results_sum = self.synchronize_async_helper(
            self.collect_service.collect(member_id="3", strategy="sum"),
        )
        results_avg = self.synchronize_async_helper(
            self.collect_service.collect(member_id="3", strategy="average"),
        )
        for result_avg, result_sum in zip(results_avg.values(), results_sum.values()):
            self.assertGreater(result_sum, result_avg), "never avg value is greater than sum value!"

    def test_results_sum(self):
        for member_id in range(10):
            member_id = str(member_id)

            results_sum = self.synchronize_async_helper(
                self.collect_service.collect(member_id=member_id, strategy="sum"),
            )
            api_results = []
            for api in self.apis:
                api_results.append(self.synchronize_async_helper(api.process(member_id=member_id)))

            strategy = FactoryStrategy.choose_strategy("sum")
            self.assertEqual(strategy.process(api_results=api_results), results_sum)

    def test_results_average(self):
        for member_id in range(10):
            member_id = str(member_id)

            results_sum = self.synchronize_async_helper(
                self.collect_service.collect(member_id=member_id, strategy="average"),
            )
            api_results = []
            for api in self.apis:
                api_results.append(self.synchronize_async_helper(api.process(member_id=member_id)))

            strategy = FactoryStrategy.choose_strategy("average")
            self.assertEqual(strategy.process(api_results=api_results), results_sum)
