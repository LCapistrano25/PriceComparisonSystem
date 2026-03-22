from pyexpat import model
from rest_framework import serializers
from core.mixins.serializers import AuditSerializerMixin
from products.models import Product, ProductPlatform, PriceAlert

class ProductSerializer(serializers.ModelSerializer, AuditSerializerMixin):

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'created_at', 'updated_at']

class ProductPlatformSerializer(serializers.ModelSerializer, AuditSerializerMixin):

    class Meta:
        model = ProductPlatform
        fields = ['id', 'product', 'platform', 'url', 'created_at', 'updated_at']

class PriceAlertSerializer(serializers.ModelSerializer, AuditSerializerMixin):

    class Meta:
        model = PriceAlert
        fields = ['id', 'product_platform', 'channel', 'min_price', 'max_price', 'created_at', 'updated_at']