from scrapers.interfaces.automation import AsyncAutomationInterface
from scrapers.browsers.playwright_automation import AsyncPlaywrightAutomation

class AutomationFactory:

    @staticmethod
    def create() -> AsyncAutomationInterface:
        return AsyncPlaywrightAutomation()