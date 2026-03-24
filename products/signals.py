from django.db.models.signals import post_save
from django.dispatch import receiver
from products.models import ProductPlatform, PriceHistory

@receiver(post_save, sender=ProductPlatform)
def create_price_history(sender, instance, **kwargs):
    history_price = PriceHistory.objects.filter(
        product_platform=instance,
        last_checked_at=instance.last_checked_at
    )

    if not history_price.exists():
        PriceHistory.objects.create(
            product_platform=instance,
            price=instance.current_price,
            last_checked_at=instance.last_checked_at
        )

