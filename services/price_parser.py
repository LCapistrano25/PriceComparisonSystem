from datetime import datetime
from django.utils import timezone

class PriceParser:

    @staticmethod
    def parse_date(date_str: str):
        naive = datetime.strptime(date_str, '%d/%m/%Y %H:%M:%S')
        return timezone.make_aware(naive)