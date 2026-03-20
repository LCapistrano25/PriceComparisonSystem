from django.db import models
from core.models.base import BaseModel
from core.enums.platforms import Platform

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

class ProductPlatform(BaseModel):
    """
    Classe para definição de plataformas de produtos
    """
    product = models.ForeignKey(
        Product, 
        related_name='platforms', 
        on_delete=models.CASCADE, 
        db_column='id_produto', 
        verbose_name='Produto'
    )

    platform = models.CharField(
        max_length=255, 
        db_column='plataforma', 
        verbose_name='Plataforma', 
        choices=Platform.choices
    )

    url = models.URLField(
        max_length=255, 
        db_column='url', 
        verbose_name='URL'
    )

    class Meta:
        db_table = 'tb_produto_plataforma'
        verbose_name = 'Plataforma de Produto'
        verbose_name_plural = 'Plataformas de Produtos'
