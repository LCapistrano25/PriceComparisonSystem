from datetime import datetime
from django.utils import timezone


def parse_date(date_str: str):
    try:
        naive = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
        return timezone.make_aware(naive)
    except ValueError as e:
        raise ValueError(f"Formato de data inválido: '{date_str}'") from e
