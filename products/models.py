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

    def __str__(self):
        return self.name

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

    current_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        db_column='preco_atual', 
        verbose_name='Preço Atual'
    )

    last_checked_at = models.DateTimeField(
        db_column='ultima_verificacao', 
        verbose_name='Última Verificação'
    )

    class Meta:
        db_table = 'tb_produto_plataforma'
        verbose_name = 'Plataforma de Produto'
        verbose_name_plural = 'Plataformas de Produtos'

    def __str__(self):
        return f"{self.product.name} - {self.platform}"

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

    def __str__(self):
        return f"{self.product_platform.product.name} - {self.channel}"

class PriceHistory(BaseModel):
    """
    Classe para definição de histórico de preços
    """
    product_platform = models.ForeignKey(
        ProductPlatform, 
        related_name='price_history', 
        on_delete=models.CASCADE, 
        db_column='id_produto_plataforma', 
        verbose_name='Plataforma de Produto'
    )

    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        db_column='preco', 
        verbose_name='Preço'
    )

    last_checked_at = models.DateTimeField(
        db_column='data_verificacao', 
        verbose_name='Data de Verificação'
    )

    class Meta:
        db_table = 'tb_historico_preco'
        verbose_name = 'Histórico de Preço'
        verbose_name_plural = 'Históricos de Preço'

    def __str__(self):
        return f"{self.product_platform.product.name} - {self.last_checked_at}"
