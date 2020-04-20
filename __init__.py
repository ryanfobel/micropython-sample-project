from supervisor import BaseApp
import uasyncio as asyncio


class App(BaseApp):
    # Setup
    def __init__(self):
        super().__init__()

    # This function runs continuously
    async def loop(self):
        print('[%s] state=%s' % (self.__module__, self._state))
        await asyncio.sleep(10)
