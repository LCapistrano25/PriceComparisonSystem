import asyncio

from core.utils.logger import Log
from asgiref.sync import sync_to_async

from products.models import ProductPlatform

from products.services.price_updater import PriceUpdaterService

from scrapers.factories.automation_factory import AutomationFactory
from scrapers.factories.platform_factory import PlatformFactory

_CONCURRENCY_LIMIT = 3

class PriceCollectorService:

    async def collect_prices(self):
        Log.info("Iniciando processo global de coleta de preços", __name__)
        items = await sync_to_async(list)(ProductPlatform.objects.all())

        if not items:
            Log.info("Nenhum item encontrado para coleta", __name__)
            return

        Log.info(f"Encontrados {len(items)} itens para processamento", __name__)

        updater = PriceUpdaterService()
        semaphore = asyncio.Semaphore(_CONCURRENCY_LIMIT)

        await asyncio.gather(*[self._process_item(item, updater, semaphore) for item in items])

        Log.info("Processo global de coleta de preços finalizado", __name__)

    async def _process_item(self, item: ProductPlatform, updater: PriceUpdaterService, semaphore: asyncio.Semaphore):
        if not item.platform or not item.url:
            Log.warning(f"Item {item.id} ignorado por falta de plataforma ou URL", __name__)
            return

        async with semaphore:
            try:
                Log.info(f"Processando item {item.id} - Plataforma: {item.platform}", __name__)
                automation = AutomationFactory.create()
                platform = PlatformFactory(automation).get(item.platform)

                data = await platform.get_info(item.url)

                if data and 'error' not in data:
                    await updater.process(item, data)
                else:
                    error_msg = data.get('error', 'Erro desconhecido') if data else 'Sem resposta da plataforma'
                    Log.error(f"Falha na coleta do item {item.id}: {error_msg}", __name__)

            except Exception as e:
                Log.error(f"Erro crítico ao processar item {item.id}: {str(e)}", __name__, exc_info=True)
