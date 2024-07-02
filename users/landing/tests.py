from rest_framework.test import APITestCase, APIClient

from users.models import UserContactApplication, User


class UserContactTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(email='test@mail.com', password='test')

    def test_user_contacts_create(self):
        self.client.login(email='test@mail.com', password='test')
        user_contacts_count = UserContactApplication.objects.count()
        data = {
            'full_name': 'Test Test',
            'phone': '+98551235'
        }
        response = self.client.post('http://127.0.0.1:8000/api/v1/landing/users/user_contacts/create/', data=data)

        user_contacts_count = UserContactApplication.objects.count()

        self.assertEqual(response.status_code, 201)
        self.assertEqual(user_contacts_count, 1)