from django.test import Client, TestCase
from django.urls import reverse


class SolutionsURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_clearbank_url(self):
        response = self.client.get('/solutions/clearbank/')
        self.assertEqual(response.status_code, 200)

    def test_clearbank_reversed_url(self):
        response = self.client.get(reverse('solutions:clearbank'))
        self.assertEqual(response.status_code, 200)

    def test_challenger_banks_url(self):
        response = self.client.get('/solutions/challenger-banks/')
        self.assertEqual(response.status_code, 200)

    def test_challenger_banks_reversed_url(self):
        response = self.client.get(reverse('solutions:challenger_banks'))
        self.assertEqual(response.status_code, 200)

    def test_railsr_banks_url(self):
        response = self.client.get('/solutions/railsr/')
        self.assertEqual(response.status_code, 200)

    def test_railsr_reversed_url(self):
        response = self.client.get(reverse('solutions:railsr'))
        self.assertEqual(response.status_code, 200)
