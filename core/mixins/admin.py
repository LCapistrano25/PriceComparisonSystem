class AuditAdminMixin:
    def save_model(self, request, obj, form, change):
        user = request.user

        if not change and not obj.created_by:
            obj.created_by = user

        obj.updated_by = user

        super().save_model(request, obj, form, change)
    
    readonly_fields = ('created_by', 'updated_by', 'created_at', 'updated_at')