from django.test import Client, TestCase
from django.urls import reverse


class LandingsURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_reversed_url(self):
        response = self.client.get(reverse('landings:home'))
        self.assertEqual(response.status_code, 200)

    def test_company_url(self):
        response = self.client.get('/company/')
        self.assertEqual(response.status_code, 200)

    def test_company_reversed_url(self):
        response = self.client.get(reverse('landings:company'))
        self.assertEqual(response.status_code, 200)

    def test_developers_url(self):
        response = self.client.get('/developers/')
        self.assertEqual(response.status_code, 200)

    def test_developers_reversed_url(self):
        response = self.client.get(reverse('landings:developers'))
        self.assertEqual(response.status_code, 200)

    def test_contacts_url(self):
        response = self.client.get('/contacts/')
        self.assertEqual(response.status_code, 200)

    def test_contacts_reversed_url(self):
        response = self.client.get(reverse('landings:contacts'))
        self.assertEqual(response.status_code, 200)
