import re
from decimal import Decimal, InvalidOperation

def parse_price(text: str) -> Decimal:
    value = re.sub(r'[^\d.,]', '', text)

    if not value:
        return Decimal('0.00')

    if ',' in value:
        value = value.replace('.', '').replace(',', '.')
    else:
        parts = value.split('.')
        if len(parts) > 1:
            value = ''.join(parts[:-1]) + '.' + parts[-1]

    try:
        return Decimal(value)
    except InvalidOperation:
        return Decimal('0.00')