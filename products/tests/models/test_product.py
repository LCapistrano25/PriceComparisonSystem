from django.test import TestCase
from products.models import Product

class TestProduct(TestCase):
    def test_product_str(self):
        product = Product.objects.create(name="Test Product", description="Description")
        self.assertEqual(str(product), "Test Product")

    def test_product_fields(self):
        product = Product.objects.create(name="Test Product", description="Description")
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Description")
        self.assertTrue(product.created_at)
        self.assertTrue(product.updated_at)
