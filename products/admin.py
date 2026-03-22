from django.contrib import admin
from core.mixins.admin import AuditAdminMixin
from products.models import Product, ProductPlatform, PriceAlert

@admin.register(Product)
class ProductAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'created_at', 'updated_at']
    search_fields = ['name', 'description']
    list_filter = ['created_at', 'updated_at']

    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Audit', {
            'fields': ('created_at', 'created_by', 'updated_at', 'updated_by'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ProductPlatform)
class ProductPlatformAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'product', 'platform', 'created_at', 'updated_at']
    search_fields = ['product__name', 'platform__name']
    list_filter = ['created_at', 'updated_at']

    fieldsets = (
        (None, {
            'fields': ('product', 'platform', 'url')
        }),
        ('Audit', {
            'fields': ('created_at', 'created_by', 'updated_at', 'updated_by'),
            'classes': ('collapse',)
        }),
    )

@admin.register(PriceAlert)
class PriceAlertAdmin(AuditAdminMixin, admin.ModelAdmin):
    list_display = ['id', 'product_platform', 'channel', 'min_price', 'max_price', 'created_at', 'updated_at']
    search_fields = ['product_platform__product__name', 'channel__name']
    list_filter = ['created_at', 'updated_at']

    fieldsets = (
        (None, {
            'fields': ('product_platform', 'channel', 'min_price', 'max_price')
        }),
        ('Audit', {
            'fields': ('created_at', 'created_by', 'updated_at', 'updated_by'),
            'classes': ('collapse',)
        }),
    )
