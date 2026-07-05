from core.utils.logger import Log
from scrapers.dto.price_collected import PriceCollected
from scrapers.dto.exception import ExceptionModel

from scrapers.interfaces.automation import AsyncAutomationInterface
from scrapers.interfaces.platform import AsyncPlatformInterface
from core.utils.format_values import parse_price

XPATH_CONTAINER = "[id^='price-final-label']"

class AsyncMagaluPlatform(AsyncPlatformInterface):
    def __init__(self, automation: AsyncAutomationInterface):
        self.automation = automation

    async def get_info(self, url: str) -> dict:
        Log.info(f"Iniciando coleta no Magalu: {url}", __name__)
        try:            
            await self.automation.start(url)
            price_text = await self.automation.get_text(XPATH_CONTAINER)
            price = parse_price(price_text)
            
            Log.info(f"Coleta finalizada com sucesso no Magalu. Preço: {price}", __name__)
            return PriceCollected(platform='Magalu', price=price).to_dict()

        except Exception as e:
            Log.error(f"Erro ao coletar dados no Magalu ({url}): {str(e)}", __name__, exc_info=True)
            return ExceptionModel(error=str(e)).to_dict()
            
        finally:
            await self.automation.stop()
