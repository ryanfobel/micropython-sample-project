from supervisor import BaseService
import uasyncio as asyncio


class Service(BaseService):
    # Setup
    def __init__(self):
        super().__init__()

    # This function runs continuously
    async def loop(self):
        self.logger.debug('state=%s' % self.state)
        await asyncio.sleep(60)
