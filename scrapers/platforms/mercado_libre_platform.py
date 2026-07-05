from core.utils.logger import Log
from scrapers.dto.exception import ExceptionModel
from scrapers.dto.price_collected import PriceCollected

from scrapers.interfaces.automation import AsyncAutomationInterface
from scrapers.interfaces.platform import AsyncPlatformInterface
from core.utils.format_values import parse_price

XPATH_CONTAINER = "//div[contains(@class, 'ui-pdp-price__second-line')]//span[contains(@class, 'ui-pdp-price__part__container')]"

class AsyncMercadoLibrePlatform(AsyncPlatformInterface):
    def __init__(self, automation: AsyncAutomationInterface):
        self.automation = automation

    async def get_info(self, url: str) -> dict:
        Log.info(f"Iniciando coleta no Mercado Livre: {url}", __name__)
        try:            
            await self.automation.start(url)
            price_text = await self.automation.get_text(XPATH_CONTAINER)
            price = parse_price(price_text.replace('\n', '').strip())
            
            Log.info(f"Coleta finalizada com sucesso no Mercado Livre. Preço: {price}", __name__)
            return PriceCollected(platform='Mercado Livre', price=price).to_dict()

        except Exception as e:
            Log.error(f"Erro ao coletar dados no Mercado Livre ({url}): {str(e)}", __name__, exc_info=True)
            return ExceptionModel(error=str(e)).to_dict()
            
        finally:
            await self.automation.stop()
            