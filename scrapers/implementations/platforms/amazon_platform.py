from core.utils.logger import Log
from scrapers.database.exceptions.exception import ExceptionModel
from scrapers.database.price_collected import PriceCollected
from scrapers.interfaces.base.automation import AsyncAutomationInterface
from scrapers.interfaces.platforms.platform import AsyncPlatformInterface

from core.utils.format_values import parse_price

XPATH_CONTAINER = "//span[contains(@class, 'a-price aok-align-center reinventPricePriceToPayMargin priceToPay apex-pricetopay-value')]"

class AsyncAmazonPlatform(AsyncPlatformInterface):
    def __init__(self, automation: AsyncAutomationInterface) -> None:
        self.automation = automation

    async def get_info(self, url: str) -> dict:
        Log.info(f"Iniciando coleta na Amazon: {url}", __name__)
        try:
            await self.automation.start(url)
            price_text = await self.automation.get_text(XPATH_CONTAINER)
            price = parse_price(price_text.replace('\n', '').strip())
            
            Log.info(f"Coleta finalizada com sucesso na Amazon. Preço: {price}", __name__)
            return PriceCollected(platform='Amazon', price=price).to_dict()
            
        except Exception as e:
            Log.error(f"Erro ao coletar dados na Amazon ({url}): {str(e)}", __name__, exc_info=True)
            return ExceptionModel(error=str(e)).to_dict()
        finally:
            await self.automation.stop()
