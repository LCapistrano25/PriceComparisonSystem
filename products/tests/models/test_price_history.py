from django.test import TestCase
from products.models import Product, ProductPlatform, PriceHistory
from decimal import Decimal
from django.utils import timezone

class TestPriceHistory(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="Description")
        self.platform_item = ProductPlatform.objects.create(
            product=self.product,
            platform="AMAZON",
            url="https://amazon.com/test",
            current_price=Decimal("100.00"),
            last_checked_at=timezone.now()
        )

    def test_price_history_fields(self):
        history = PriceHistory.objects.create(
            product_platform=self.platform_item,
            price=Decimal("120.00"),
            last_checked_at=timezone.now()
        )
        self.assertEqual(history.product_platform, self.platform_item)
        self.assertEqual(history.price, Decimal("120.00"))
        self.assertTrue(history.last_checked_at)
