
from products.models import ProductPlatform

class PriceAlertService:
    
    async def process(self, item: ProductPlatform, data: dict):
        if not data:
            return