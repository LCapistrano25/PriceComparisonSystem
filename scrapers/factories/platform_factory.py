from core.enums.platforms import Platform

from scrapers.interfaces.automation import AsyncAutomationInterface

from scrapers.platforms.amazon_platform import AsyncAmazonPlatform
from scrapers.platforms.mercado_libre_platform import AsyncMercadoLibrePlatform
from scrapers.platforms.magalu_platform import AsyncMagaluPlatform


class PlatformFactory:

    def __init__(self, automation: AsyncAutomationInterface):
        self.automation = automation

    def get(self, platform: Platform):
        if platform == Platform.AMAZON:
            return AsyncAmazonPlatform(self.automation)

        if platform == Platform.MAGALU:
            return AsyncMagaluPlatform(self.automation)

        if platform == Platform.MERCADOLIVRE:
            return AsyncMercadoLibrePlatform(self.automation)

        raise ValueError("Plataforma inválida")
    
    def get_by_url(self, url: str):
        if "amazon.com.br" in url:
            return AsyncAmazonPlatform(self.automation)

        if "mercadolivre.com.br" in url:
            return AsyncMercadoLibrePlatform(self.automation)

        if "magazineluiza.com.br" in url:
            return AsyncMagaluPlatform(self.automation)

        raise ValueError("Plataforma inválida")