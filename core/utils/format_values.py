import re
from decimal import Decimal, InvalidOperation

def parse_price(text: str) -> Decimal:
    if not text:
        return Decimal('0.00')

    # Remove tudo que não for dígito, ponto ou vírgula
    value = re.sub(r'[^\d.,]', '', text)

    if not value:
        return Decimal('0.00')

    # Se houver vírgula, tratamos como formato brasileiro (1.199,00)
    if ',' in value:
        value = value.replace('.', '').replace(',', '.')
    else:
        # Se não houver vírgula, mas houver ponto(s)
        if '.' in value:
            parts = value.split('.')
            # Se o último bloco após o ponto tiver exatamente 3 dígitos, 
            # é muito provável que seja um separador de milhar (ex: 1.199)
            if len(parts[-1]) == 3:
                value = value.replace('.', '')
            else:
                # Caso contrário, tratamos o ponto como decimal (ex: 10.5 ou 10.50)
                pass

    try:
        return Decimal(value)
    except InvalidOperation:
        return Decimal('0.00')