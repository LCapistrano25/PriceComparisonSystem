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