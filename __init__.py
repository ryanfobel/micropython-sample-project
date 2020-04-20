from supervisor import BaseApp
import uasyncio as asyncio


class App(BaseApp):
    # Setup
    def __init__(self, name):
        super().__init__(name)

    # This function runs continuously
    async def loop(self):
        print('[%s] state=%s' % (self.name, self._state))
        await asyncio.sleep(10)
