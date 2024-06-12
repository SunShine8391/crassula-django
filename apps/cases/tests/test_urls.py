from django.test import Client, TestCase
from django.urls import reverse


class CasesURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_paysend_url(self):
        response = self.client.get('/cases/paysend/')
        self.assertEqual(response.status_code, 200)

    def test_paysend_reversed_url(self):
        response = self.client.get(reverse('cases:paysend'))
        self.assertEqual(response.status_code, 200)

    def test_safe_currency_url(self):
        response = self.client.get('/cases/safe-currency/')
        self.assertEqual(response.status_code, 200)

    def test_safe_currency_reversed_url(self):
        response = self.client.get(reverse('cases:safe_currency'))
        self.assertEqual(response.status_code, 200)
