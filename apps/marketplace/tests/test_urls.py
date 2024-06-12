from django.test import TestCase, Client
from django.urls import reverse
from apps.marketplace.models import Category, App


class MarketplaceURLTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_marketplace_main_url(self):
        client = Client()
        response = client.get('/marketplace/')
        self.assertEqual(response.status_code, 200)


    def test_marketplace_main_reversed_url(self):
        response = self.client.get(reverse('marketplace:main'))
        self.assertEqual(response.status_code, 200)

class AppDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.category = Category.objects.create(
            name='Test Category',
            slug='test-category',
            seo_title='Test Category',
            seo_description='This is a test category'
        )
        self.app = App.objects.create(
            name='Test App',
            slug='test-app',
            seo_title='Test App',
            seo_description='This is a test app',
            small_description='This is a test app',
            full_description='This is a test app',
        )
        self.app.categories.add(self.category)

    def test_app_detail_view(self):
        url = reverse('marketplace:app', kwargs={'slug': self.app.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.app.name)
        self.assertContains(response, self.app.seo_title)
        self.assertContains(response, self.app.seo_description)
        self.assertContains(response, self.app.small_description)
        self.assertContains(response, self.app.full_description)
        self.assertContains(response, self.app.slug)
