from rest_framework.test import APITestCase, APIClient
from order.models import Order
from products.models import Product
from users.models import User


class OrderTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(email='test@mail.com', password='test')
        self.product = Product.objects.create(name='test', content='test', price='1000')
        self.customuser = User.objects.create_user(email='test1@mail.com', password='test')
        Order.objects.create(
            product=self.product,
            count=10, free_count=1,
            customer=self.customuser,
            longitude=1.0,
            latitude=1.0,
            status='created',
            product_price=10000,
            total_price=1000000,
            admin=self.user
        )
        self.client.login(email='test@mail.com', password='test')

    def test_all_get_orders(self):
        response = self.client.get('/api/v1/admin/orders/orders/')

        self.assertEqual(response.status_code, 200)

    def test_patch_order(self):
        data = {
            'status': 'delivered',
        }
        response = self.client.patch('/api/v1/admin/orders/orders/1/', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'delivered')

        response = self.client.put('/api/v1/admin/orders/orders/1/', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['status'], 'delivered')

    def test_get_order(self):
        response = self.client.get('/api/v1/admin/orders/orders/1/')

        self.assertEqual(response.status_code, 200)

