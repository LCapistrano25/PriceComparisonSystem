from django.test import TestCase
from products.models import Product, ProductPlatform
from decimal import Decimal
from django.utils import timezone

class TestProductPlatform(TestCase):
    def setUp(self):
        self.product = Product.objects.create(name="Test Product", description="Description")
        self.platform_item = ProductPlatform.objects.create(
            product=self.product,
            platform="AMAZON",
            url="https://amazon.com/test",
            current_price=Decimal("100.00"),
            last_checked_at=timezone.now()
        )

    def test_product_platform_fields(self):
        self.assertEqual(self.platform_item.product, self.product)
        self.assertEqual(self.platform_item.platform, "AMAZON")
        self.assertEqual(self.platform_item.url, "https://amazon.com/test")
        self.assertEqual(self.platform_item.current_price, Decimal("100.00"))
        self.assertTrue(self.platform_item.last_checked_at)
