import asyncio
from celery import shared_task

@shared_task(bind=True)
def scrape_product() -> None:
    from services.price_collector import PriceCollectorService
    print('Scrape product task started')
    price_collector = PriceCollectorService()
    asyncio.run(price_collector.collect_prices())
    print('Scrape product task finished')