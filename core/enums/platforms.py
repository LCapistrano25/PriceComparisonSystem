from django.db import models

class Platform(models.TextChoices):
    AMAZON = 'AMAZON', 'Amazon'
    MERCADOLIVRE = 'MERCADOLIVRE', 'Mercado Livre'
    CASASBAHIA = 'CASASBAHIA', 'Casas Bahia'
    MAGALU = 'MAGALU', 'Magalu'