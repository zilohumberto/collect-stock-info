import unittest
import asyncio


class TestBase(unittest.TestCase):

    def synchronize_async_helper(self, to_await):
        async_response = []

        async def run_and_capture_result():
            r = await to_await
            async_response.append(r)

        loop = asyncio.get_event_loop()
        coroutine = run_and_capture_result()
        loop.run_until_complete(coroutine)
        return async_response[0]
