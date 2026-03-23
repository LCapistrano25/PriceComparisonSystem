from abc import ABC, abstractmethod

class AsyncPlatformInterface(ABC):

    @abstractmethod
    async def execute(self):
        pass
