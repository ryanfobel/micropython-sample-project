from supervisor import BaseService
import uasyncio as asyncio


class Service(BaseService):
    # Setup
    def __init__(self):
        super().__init__()

    # This function runs continuously
    async def loop(self):
        print('[%s] state=%s' % (self.__module__, self.state))
        await asyncio.sleep(10)
