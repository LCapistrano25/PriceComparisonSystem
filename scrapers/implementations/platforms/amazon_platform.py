from datetime import datetime
from scrapers.interfaces.base.automation import AsyncAutomationInterface
from scrapers.interfaces.platforms.platform import AsyncPlatformInterface

from core.utils.format_values import parse_price

XPATH_CONTAINER = "//span[contains(@class, 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay apex-pricetopay-value')]"

class AsyncAmazonPlatform(AsyncPlatformInterface):
    def __init__(self, automation: AsyncAutomationInterface) -> None:
        self.automation = automation

    async def get_info(self, url: str) -> dict:
        try:
            await self.automation.start(url)
            price_text = await self.automation.get_text(XPATH_CONTAINER)
            return {
                'platform': 'Amazon',
                'price': parse_price(price_text.replace('\n', '').strip()),
                'consult_date': datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            }
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return {
                'error': e
            }
        finally:
            await self.automation.stop()
