from abc import ABC, abstractmethod

class AsyncAutomationInterface(ABC):
    
    @abstractmethod
    async def start(self, url: str) -> None:
        pass

    @abstractmethod
    async def get_text(self, field: str, timeout: int = 10000) -> str:
        pass

    @abstractmethod
    async def stop(self) -> None:
        pass