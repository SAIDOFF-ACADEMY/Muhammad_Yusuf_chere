from rest_framework.test import APITestCase, APIClient
from common.models import Settings, Page, GalleryPhoto


class SettingsTestCase(APITestCase):
    def setUp(self):
        self.settings = Settings.objects.create(
            contact_telegram='test',
            contact_phone='95516516',
            longitude=02132.0,
            latitude=32103.351,
            location_text='test',
            working_hours_start='12:00',
            working_hours_end='12:00',
            telegram_bot='testbot'
        )

    def test_get_settings(self):
        response = self.client.get('/api/v1/landing/common/settings/')

        self.assertEqual(response.status_code, 200)


class GalleryPhotoTestCase(APITestCase):
    def setUp(self):
        self.photo = GalleryPhoto.objects.create(
            photo="http://127.0.0.1:8000/media/photos/2024/06/Chere_sayt_TZ.pdf"
        )

    def test_get_photos(self):
        response = self.client.get('/api/v1/landing/common/photos/')

        self.assertEqual(response.status_code, 200)


class PageTestCase(APITestCase):
    def setUp(self):
        self.page = Page.objects.create(
            title='test',
            slug='test',
            content='test',
        )

    def test_get_page_with_slug(self):
        response = self.client.get('/api/v1/landing/common/page/test/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'test')

        response = self.client.get('/api/v1/landing/common/page/1/')

        self.assertEqual(response.status_code, 404)


