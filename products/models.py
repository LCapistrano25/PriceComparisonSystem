from django.db import models
from core.models.base import BaseModel
from core.enums.platforms import Platform
from core.enums.channels import Channel

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

class PriceAlert(BaseModel):
    """
    Classe para definição de alertas de preço
    """
    product_platform = models.ForeignKey(
        ProductPlatform, 
        related_name='alerts', 
        on_delete=models.CASCADE, 
        db_column='id_produto_plataforma', 
        verbose_name='Plataforma de Produto'
    )

    channel = models.CharField(
        max_length=255, 
        db_column='canal', 
        verbose_name='Canal', 
        choices=Channel.choices
    )

    min_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        db_column='preco_minimo', 
        verbose_name='Preço Mínimo'
    )

    max_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        db_column='preco_maximo', 
        verbose_name='Preço Máximo'
    )

    is_active = models.BooleanField(
        db_column='ativo', 
        verbose_name='Ativo', 
        default=True
    )

    class Meta:
        db_table = 'tb_alerta_preco'
        verbose_name = 'Alerta de Preço'
        verbose_name_plural = 'Alertas de Preço'