from datetime import datetime
from interfaces.base.automation import AsyncAutomationInterface
from interfaces.platforms.platform import AsyncPlatformInterface

XPATH_CONTAINER = "//span[contains(@class, 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay apex-pricetopay-value')]"
X
class AsyncAmazonPlatform(AsyncPlatformInterface):
    def __init__(self, automation: AsyncAutomationInterface, url: str) -> None:
        self.automation = automation
        self.url = url

    async def execute(self) -> dict:
        try:
            await self.automation.start(self.url)
            price_text = await self.automation.get_text(XPATH_CONTAINER)
            return {
                'platform': 'Amazon',
                'price': price_text.replace('\n', '').strip(),
                'consult_date': datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            }
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            return {
                'error': e
            }
        finally:
            await self.automation.stop()