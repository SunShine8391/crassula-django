from django.test import Client, TestCase
from django.urls import reverse


class CareersURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_career_main_url(self):
        response = self.client.get('/careers/')
        self.assertEqual(response.status_code, 200)

    def test_career_main_reversed_url(self):
        response = self.client.get(reverse('careers:main'))
        self.assertEqual(response.status_code, 200)
