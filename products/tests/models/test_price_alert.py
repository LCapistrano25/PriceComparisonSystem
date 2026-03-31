from django.test import TestCase
from products.models import Product, ProductPlatform, PriceAlert
from decimal import Decimal
from django.utils import timezone

class TestPriceAlert(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="Description")
        self.platform_item = ProductPlatform.objects.create(
            product=self.product,
            platform="AMAZON",
            url="https://amazon.com/test",
            current_price=Decimal("100.00"),
            last_checked_at=timezone.now()
        )

    def test_price_alert_fields(self):
        alert = PriceAlert.objects.create(
            product_platform=self.platform_item,
            channel="EMAIL",
            min_price=Decimal("50.00"),
            max_price=Decimal("150.00"),
            is_active=True
        )
        self.assertEqual(alert.product_platform, self.platform_item)
        self.assertEqual(alert.channel, "EMAIL")
        self.assertEqual(alert.min_price, Decimal("50.00"))
        self.assertEqual(alert.max_price, Decimal("150.00"))
        self.assertTrue(alert.is_active)
