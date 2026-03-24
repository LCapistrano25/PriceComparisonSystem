from asgiref.sync import sync_to_async
from datetime import datetime
from django.utils import timezone
from products.models import ProductPlatform, PriceHistory

from scrapers.factories.automation_factory import AutomationFactory
from scrapers.factories.platform_factory import PlatformFactory
from scrapers.interfaces.base import automation

class PriceCollectorService:

    async def collect_prices(self):
        items = await sync_to_async(list)(ProductPlatform.objects.all())
        automation = AutomationFactory.create()
    
        for item in items:
            platform_name = item.platform
            url = item.url

            if not platform_name:
                continue

            if not url:
                continue
            
            try:
                factory = PlatformFactory(automation).get(platform_name)
                resp = await factory.get_info(url)
                
                if resp and 'price' in resp and 'consult_date' in resp:
                    platform_price = resp['price']
                    platform_consult_date_str = resp['consult_date']
                    platform_consult_date_naive = datetime.strptime(platform_consult_date_str, '%d/%m/%Y %H:%M:%S')
                    platform_consult_date = timezone.make_aware(platform_consult_date_naive)
                    
                    # Check if price has changed
                    if platform_price != item.current_price:
                        # Save PriceHistory and Update ProductPlatform using sync_to_async
                        await sync_to_async(PriceHistory.objects.create)(
                            product_platform=item,
                            price=platform_price,
                            last_checked_at=platform_consult_date
                        )
                        item.current_price = platform_price
                        item.last_checked_at = platform_consult_date
                        await sync_to_async(item.save)()
            except Exception as e:
                print(e)

    