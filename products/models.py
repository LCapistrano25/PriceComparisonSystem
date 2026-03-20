from django.db import models
from core.models.base import BaseModel

class Product(BaseModel):
    """
    Classe para definição de produtos
    """
    name = models.CharField(
        max_length=255, 
        db_column='nome', 
        verbose_name='Nome'
    )

    description = models.TextField(
        db_column='descricao', 
        verbose_name='Descrição'
    )

    class Meta:
        db_table = 'tb_produto'
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
