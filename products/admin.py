from django.contrib import admin
from core.mixins.admin import AuditAdminMixin
from products.models import Product

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
