from decimal import Decimal

from django.utils import timezone
from core.utils.logger import Log

from asgiref.sync import sync_to_async

from products.models import PriceHistory, ProductPlatform
from products.utils import parse_date

class PriceUpdaterService:

    async def process(self, item: ProductPlatform, data: dict):
        if not data:
            Log.warning(f"Processamento de atualização ignorado para item {item.id}: dados vazios", __name__)
            return

        if 'price' not in data or 'consult_date' not in data:
            Log.warning(f"Dados incompletos recebidos para item {item.id}: {data}", __name__)
            return

        price = data['price']
        consult_date = parse_date(data['consult_date'])

        if price == item.current_price:
            Log.info(f"Preço do item {item.id} mantido (sem alteração): {price}", __name__)
            return

        Log.info(f"Alteração de preço detectada para item {item.id}: {item.current_price} -> {price}", __name__)
        await self._update(item, price, consult_date)

    async def _update(self, item: ProductPlatform, price: Decimal, consult_date: timezone.datetime):
        try:
            await sync_to_async(PriceHistory.objects.create)(
                product_platform=item,
                price=price,
                last_checked_at=consult_date
            )

            item.current_price = price
            item.last_checked_at = consult_date

            await sync_to_async(item.save)()
            Log.info(f"Item {item.id} atualizado com sucesso no banco de dados", __name__)

        except Exception as e:
            Log.error(f"Erro ao salvar atualização do item {item.id} no banco: {str(e)}", __name__, exc_info=True)
            raise
