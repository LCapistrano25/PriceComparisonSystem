from datetime import datetime
from scrapers.interfaces.base.automation import AsyncAutomationInterface
from scrapers.interfaces.platforms.platform import AsyncPlatformInterface
from core.utils.format_values import parse_price

XPATH_CONTAINER = "[id^='price-final-label']"

class AsyncMagaluPlatform(AsyncPlatformInterface):
    def __init__(self, automation: AsyncAutomationInterface, url: str):
        self.automation = automation
        self.url = url

    async def execute(self):
        try:            
            await self.automation.start(self.url)
            price_text = await self.automation.get_text(XPATH_CONTAINER)
            return {
                'platform': 'Magalu',
                'price': parse_price(price_text),
                'consult_date': datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            }
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return {
                'error': e
            }
        finally:
            await self.automation.stop()