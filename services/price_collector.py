from asgiref.sync import sync_to_async

from products.models import ProductPlatform

from services.price_updater import PriceUpdaterService

from scrapers.factories.automation_factory import AutomationFactory
from scrapers.factories.platform_factory import PlatformFactory

class PriceCollectorService:

    async def collect_prices(self):
        items = await sync_to_async(list)(ProductPlatform.objects.all())
        automation = AutomationFactory.create()

        for item in items:
            if not item.platform or not item.url:
                continue

            try:
                platform = PlatformFactory(automation).get(item.platform)

                data = await platform.get_info(item.url)

                await PriceUpdaterService().process(item, data)
            except Exception as e:
                print(e)
                continue