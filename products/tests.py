from rest_framework.test import APITestCase, APIClient
from users.models import User
from products.models import Product, FreeProduct


class ProductTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(email='test@mail.com', password='test')

    def test_all_products(self):
        self.client.login(email='test@mail.com', password='test')
        Product.objects.create(name='test', content='test', price='1000')
        Product.objects.create(name='test1', content='test1', price='10001')
        Product.objects.create(name='test2', content='test2', price='10002')

        response = self.client.get('/api/v1/admin/products/products/')

        products = Product.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(products, 3)

    def test_delete_product(self):
        self.client.login(email='test@mail.com', password='test')
        Product.objects.create(name='test', content='test', price='1000')

        response = self.client.delete('/api/v1/admin/products/product/1/')
        products = Product.objects.count()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(products, 0)

    def test_path_product(self):
        self.client.login(email='test@mail.com', password='test')
        Product.objects.create(name='test', content='test', price='1000')

        response = self.client.patch('/api/v1/admin/products/product/1/', data={
            'name': 'test1'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test1')

    def test_put_product(self):
        self.client.login(email='test@mail.com', password='test')
        Product.objects.create(name='test', content='test', price='1000')
        data = {
            'name': 'test1',
            'content': 'test1',
            'price': '1500'
        }
        response = self.client.patch('/api/v1/admin/products/product/1/', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test1')
        self.assertEqual(response.data['content'], 'test1')
        self.assertEqual(response.data['price'], 1500)

    def test_get_product(self):
        self.client.login(email='test@mail.com', password='test')
        Product.objects.create(name='test', content='test', price='1000')

        response = self.client.get('/api/v1/admin/products/product/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'test'),
        self.assertEqual(response.data['content'], 'test'),
        self.assertEqual(response.data['price'], 1000),

    def test_create_product(self):
        self.client.login(email='test@mail.com', password='test')
        data = {
            'name': 'test',
            'name_uz': 'test',
            'name_ru': 'test',
            'content': 'test',
            'content_uz': 'test',
            'content_ru': 'test',
            'price': '4000',
        }
        response = self.client.post('/api/v1/admin/products/product/create/', data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['name_uz'], 'test')
        self.assertEqual(response.data['name_ru'], 'test')
        self.assertEqual(response.data['content_uz'], 'test')
        self.assertEqual(response.data['content_ru'], 'test')
        self.assertEqual(response.data['price'], 4000)
        self.assertEqual(response.data['content'], 'test')
        self.assertEqual(response.data['name'], 'test')


class FreeProductTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(email='test@mail.com', password='test')
        self.product = Product.objects.create(name='test', content='test', price='1000')

    def test_get_all_free_products(self):
        self.client.login(email='test@mail.com', password='test')
        FreeProduct.objects.create(product=self.product, count=10, free_count=1)
        FreeProduct.objects.create(product=self.product, count=20, free_count=12)
        FreeProduct.objects.create(product=self.product, count=210, free_count=112)

        response = self.client.get('/api/v1/admin/products/free_products/')

        free_product = FreeProduct.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(free_product, 3)

    def test_delete_free_product(self):
        self.client.login(email='test@mail.com', password='test')
        FreeProduct.objects.create(product=self.product, count=10, free_count=1)

        response = self.client.delete('/api/v1/admin/products/free_product/1/')
        free_product = FreeProduct.objects.count()

        self.assertEqual(response.status_code, 204)
        self.assertEqual(free_product, 0)

    def test_patch_free_product(self):
        self.client.login(email='test@mail.com', password='test')
        FreeProduct.objects.create(product=self.product, count=10, free_count=1)
        data = {
            'count': 9
        }
        response = self.client.patch('/api/v1/admin/products/free_product/1/', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 9)

    def test_put_free_product(self):
        self.client.login(email='test@mail.com', password='test')
        product = Product.objects.create(name='test', content='test', price='1000')
        FreeProduct.objects.create(product=self.product, count=10, free_count=1)
        data = {
            'product': product.id,
            'count': 9,
            'free_count': 0
        }
        response = self.client.put('/api/v1/admin/products/free_product/1/', data=data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 9)
        self.assertEqual(response.data['free_count'], 0)

    def test_get_free_product(self):
        self.client.login(email='test@mail.com', password='test')
        FreeProduct.objects.create(product=self.product, count=10, free_count=1)

        response = self.client.get('/api/v1/admin/products/free_product/1/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['count'], 10)
        self.assertEqual(response.data['free_count'], 1)

    def test_create_free_product(self):
        self.client.login(email='test@mail.com', password='test')

        data = {
            'product': self.product.id,
            'count': 100,
            'free_count': 10,
        }
        response = self.client.post('/api/v1/admin/products/free_product/create/', data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['count'], 100)
        self.assertEqual(response.data['free_count'], 10)