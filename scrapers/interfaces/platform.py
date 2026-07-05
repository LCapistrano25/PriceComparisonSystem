from abc import ABC, abstractmethod

class AsyncPlatformInterface(ABC):

    @abstractmethod
    async def get_info(self, url: str) -> dict:
        pass
