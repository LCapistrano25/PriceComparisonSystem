class AuditSerializerMixin:
    def create(self, validated_data):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if user:
            validated_data['created_by'] = user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        request = self.context.get('request')
        user = getattr(request, 'user', None)
        if user:
            validated_data['updated_by'] = user
        return super().update(instance, validated_data)