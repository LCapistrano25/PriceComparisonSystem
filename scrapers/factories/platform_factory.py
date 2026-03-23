from core.enums.platforms import Platform

from scrapers.interfaces.base.automation import AsyncAutomationInterface

from scrapers.implementations.platforms.amazon_platform import AsyncAmazonPlatform
from scrapers.implementations.platforms.mercado_libre_platform import AsyncMercadoLibrePlatform
from scrapers.implementations.platforms.magalu_platform import AsyncMagaluPlatform


class PlatformFactory:

    def __init__(self, automation: AsyncAutomationInterface):
        self.automation = automation

    def get(self, platform: Platform):
        if platform == Platform.AMAZON:
            return AsyncAmazonPlatform(self.automation)

        if platform == Platform.MAGALU:
            return AsyncMagaluPlatform(self.automation)

        if platform == Platform.MERCADO_LIVRE:
            return AsyncMercadoLibrePlatform(self.automation)

        raise ValueError("Plataforma inválida")