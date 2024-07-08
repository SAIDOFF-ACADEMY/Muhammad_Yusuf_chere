# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, FreeProduct


class ProductAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product1 = Product.objects.create(name='Test Product 1', price=10.0)
        self.product2 = Product.objects.create(name='Test Product 2', price=20.0)
        self.product3 = Product.objects.create(name='Test Product 3', price=30.0)
        self.free_product1 = FreeProduct.objects.create(name='Test Free Product 1')
        self.free_product2 = FreeProduct.objects.create(name='Test Free Product 2')
        self.free_product3 = FreeProduct.objects.create(name='Test Free Product 3')

    def test_product_list_view(self):
        response = self.client.get('/api/v1/admin/products/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_product_create_view(self):
        data = {'name': 'New Product', 'price': 15.0}
        response = self.client.post('/api/v1/admin/products/product/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Product')

    def test_product_detail_view(self):
        url = f'/api/v1/admin/products/product/{self.product1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.product1.name)

    def test_product_update_view(self):
        url = f'/api/v1/admin/products/product/{self.product1.id}/'
        data = {'name': 'Updated Product 1', 'price': 25.0}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product1.refresh_from_db()
        self.assertEqual(self.product1.name, 'Updated Product 1')
        self.assertEqual(self.product1.price, 25.0)

    def test_product_delete_view(self):
        url = f'/api/v1/admin/products/product/{self.product1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Product.objects.filter(id=self.product1.id).exists())

    def test_free_product_list_view(self):
        response = self.client.get('/api/v1/admin/products/free_products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_free_product_create_view(self):
        data = {'name': 'New Free Product'}
        response = self.client.post('/api/v1/admin/products/free_product/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'New Free Product')

    def test_free_product_detail_view(self):
        url = f'/api/v1/admin/products/free_product/{self.free_product1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.free_product1.name)

    def test_free_product_update_view(self):
        url = f'/api/v1/admin/products/free_product/{self.free_product1.id}/'
        data = {'name': 'Updated Free Product 1'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.free_product1.refresh_from_db()
        self.assertEqual(self.free_product1.name, 'Updated Free Product 1')

    def test_free_product_delete_view(self):
        url = f'/api/v1/admin/products/free_product/{self.free_product1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(FreeProduct.objects.filter(id=self.free_product1.id).exists())
