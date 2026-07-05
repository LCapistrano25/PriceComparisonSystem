from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class PriceCollected(BaseModel):
    platform: str
    price: Decimal
    consult_date: str = datetime.now().strftime('%d/%m/%Y %H:%M:%S')

    def to_dict(self):
        return self.model_dump()