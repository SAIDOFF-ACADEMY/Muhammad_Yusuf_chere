from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from users import models
from users.models import UserContactApplication

User = get_user_model()


class UserTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_user = User.objects.create_superuser(
            email='muhammadyusufni03@gmail.com', password='1'
        )
        self.user = User.objects.create_user(
            email='user@example.com', password='test'
        )

    def test_user_list(self):
        url = reverse('user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_detail(self):
        url = reverse('user_detail', kwargs={'id': self.user.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_create(self):
        url = reverse('user_create')
        data = {'email': 'newuser@example.com', 'password': 'testpassword'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_user_update(self):
        url = reverse('user_update', kwargs={'id': self.user.id})
        data = {'username': 'updateduser'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_user_delete(self):
        url = reverse('user_delete', kwargs={'id': self.user.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)

    def test_user_login(self):
        url = reverse('user_login')
        data = {'email': self.user.email, 'password': 'test'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)

    def test_user_logout(self):
        url = reverse('user_logout')
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_user_contact_list(self):
        url = reverse('user_contact_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_contact_update(self):
        contact = UserContactApplication.objects.create(
            user=self.user,
            full_name='Test User',
            phone='1234567890',
            message='Test message'
        )
        url = reverse('user_contact_update', kwargs={'id': contact.id})
        data = {'message': 'Updated message'}
        response = self.client.put(url, data, content_type='application/json')
        self.assertEqual(response.status_code, 200)

        # Fetch the updated contact to verify the change
        contact.refresh_from_db()
        self.assertEqual(contact.message, 'Updated message')

    def test_user_contact_detail(self):
        contact = models.UserContactApplication.objects.create(
            user=self.user, message='Test message'
        )
        url = reverse('user_contact_detail', kwargs={'id': contact.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_user_contact_delete(self):
        contact = models.UserContactApplication.objects.create(
            user=self.user, message='Test message'
        )
        url = reverse('user_contact_detail', kwargs={'id': contact.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
