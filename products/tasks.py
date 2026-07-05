import asyncio
from core.utils.logger import Log
from celery import shared_task

@shared_task
def scrape_product() -> None:
    from products.services.price_collector import PriceCollectorService
    
    Log.info("Celery Task: scrape_product iniciada", __name__)
    try:
        price_collector = PriceCollectorService()
        asyncio.run(price_collector.collect_prices())
        Log.info("Celery Task: scrape_product finalizada com sucesso", __name__)
    except Exception as e:
        Log.error(f"Celery Task: scrape_product falhou com erro: {str(e)}", __name__, exc_info=True)
        raise