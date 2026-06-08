from asyncio import Lock


class RoundRobinScheduler:

    def __init__(self):

        self.current_index = 0

        self.lock = Lock()

    async def select_server(
        self,
        services
    ):

        if not services:
            return None

        async with self.lock:

            server = services[
                self.current_index % len(services)
            ]

            self.current_index += 1

            return server