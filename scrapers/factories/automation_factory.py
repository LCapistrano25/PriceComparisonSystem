from scrapers.interfaces.base.automation import AsyncAutomationInterface
from scrapers.implementations.playwright_automation import AsyncPlaywrightAutomation

class AutomationFactory:

    @staticmethod
    def create() -> AsyncAutomationInterface:
        return AsyncPlaywrightAutomation()