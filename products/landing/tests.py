from rest_framework.test import APITestCase
from products.models import Product


class ProductTestCase(APITestCase):
    def test_all_products(self):
        Product.objects.create(name='test', content='test', price='1000')
        Product.objects.create(name='test1', content='test1', price='10001')
        Product.objects.create(name='test2', content='test2', price='10002')

        response = self.client.get('http://127.0.0.1:8000/api/v1/landing/products/products/')

        products = Product.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(products, 3)
