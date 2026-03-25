from decimal import Decimal
from django.utils import timezone

from asgiref.sync import sync_to_async
from products.models import PriceHistory, ProductPlatform
from services.price_parser import PriceParser

class PriceUpdaterService:

    async def process(self, item: ProductPlatform, data: dict):
        if not data:
            return

        if 'price' not in data or 'consult_date' not in data:
            return

        price = data['price']
        consult_date = PriceParser.parse_date(data['consult_date'])

        if price == item.current_price:
            return

        await self._update(item, price, consult_date)

    async def _update(self, item: ProductPlatform, price: Decimal, consult_date: timezone.datetime):
        await sync_to_async(PriceHistory.objects.create)(
            product_platform=item,
            price=price,
            last_checked_at=consult_date
        )

        item.current_price = price
        item.last_checked_at = consult_date

        await sync_to_async(item.save)()