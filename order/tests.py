# tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Order
from products.models import Product
from users.models import User

class OrderAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create test data
        self.product = Product.objects.create(name='Test Product', price=10.0)
        self.customer = User.objects.create_user(username='customer', password='password')
        self.admin = User.objects.create_user(username='admin', password='password')

        self.order1 = Order.objects.create(
            product=self.product,
            count=1,
            free_count=0,
            customer=self.customer,
            longitude=12.34,
            latitude=56.78,
            status=Order.Status.CREATED,
            product_price=1000,
            total_price=1000,
            admin=self.admin
        )

        self.order2 = Order.objects.create(
            product=self.product,
            count=2,
            free_count=1,
            customer=self.customer,
            longitude=12.34,
            latitude=56.78,
            status=Order.Status.IN_PROGRESS,
            product_price=1000,
            total_price=2000,
            admin=self.admin
        )

        self.order3 = Order.objects.create(
            product=self.product,
            count=3,
            free_count=2,
            customer=self.customer,
            longitude=12.34,
            latitude=56.78,
            status=Order.Status.ON_THE_WAY,
            product_price=1000,
            total_price=3000,
            admin=self.admin
        )

    def test_order_list_view(self):
        response = self.client.get('/api/v1/admin/orders/orders/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreater(len(response.data), 0)

    def test_order_create_view(self):
        data = {
            'product': self.product.id,
            'count': 5,
            'free_count': 0,
            'customer': self.customer.id,
            'longitude': 12.34,
            'latitude': 56.78,
            'status': Order.Status.CREATED,
            'product_price': 1000,
            'total_price': 5000,
            'admin': self.admin.id
        }
        response = self.client.post('/api/v1/admin/orders/orders/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['count'], 5)

    def test_order_detail_view(self):
        url = f'/api/v1/admin/orders/orders/{self.order1.id}/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], self.order1.count)

    def test_order_update_view(self):
        url = f'/api/v1/admin/orders/orders/{self.order1.id}/'
        data = {
            'product': self.product.id,
            'count': 10,
            'free_count': 1,
            'customer': self.customer.id,
            'longitude': 12.34,
            'latitude': 56.78,
            'status': Order.Status.DELIVERED,
            'product_price': 1000,
            'total_price': 10000,
            'admin': self.admin.id
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.order1.refresh_from_db()
        self.assertEqual(self.order1.count, 10)
        self.assertEqual(self.order1.status, Order.Status.DELIVERED)

    def test_order_delete_view(self):
        url = f'/api/v1/admin/orders/orders/{self.order1.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Order.objects.filter(id=self.order1.id).exists())
