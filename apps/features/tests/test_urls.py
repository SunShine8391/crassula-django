from django.test import Client, TestCase
from django.urls import reverse


class FeaturesURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_cards_url(self):
        response = self.client.get('/features/cards/')
        self.assertEqual(response.status_code, 200)

    def test_cards_reversed_url(self):
        response = self.client.get(reverse('features:cards'))
        self.assertEqual(response.status_code, 200)

    def test_prices_url(self):
        response = self.client.get('/features/prices/')
        self.assertEqual(response.status_code, 200)

    def test_prices_reversed_url(self):
        response = self.client.get(reverse('features:prices'))
        self.assertEqual(response.status_code, 200)

    def test_accounts_url(self):
        response = self.client.get('/features/accounts/')
        self.assertEqual(response.status_code, 200)

    def test_accounts_reversed_url(self):
        response = self.client.get(reverse('features:accounts'))
        self.assertEqual(response.status_code, 200)

    def test_transfers_url(self):
        response = self.client.get('/features/transfers/')
        self.assertEqual(response.status_code, 200)

    def test_transfers_reversed_url(self):
        response = self.client.get(reverse('features:transfers'))
        self.assertEqual(response.status_code, 200)

    def test_currency_exchange_url(self):
        response = self.client.get('/features/currency-exchange/')
        self.assertEqual(response.status_code, 200)

    def test_currency_exchange_reversed_url(self):
        response = self.client.get(reverse('features:currency_exchange'))
        self.assertEqual(response.status_code, 200)

    def test_crypto_url(self):
        response = self.client.get('/features/crypto/')
        self.assertEqual(response.status_code, 200)

    def test_crypto_reversed_url(self):
        response = self.client.get(reverse('features:crypto'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_url(self):
        response = self.client.get('/features/dashboard/')
        self.assertEqual(response.status_code, 200)

    def test_dashboard_reversed_url(self):
        response = self.client.get(reverse('features:dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_ui_url(self):
        response = self.client.get('/features/ui/')
        self.assertEqual(response.status_code, 200)

    def test_ui_reversed_url(self):
        response = self.client.get(reverse('features:ui'))
        self.assertEqual(response.status_code, 200)

    def test_compliance_url(self):
        response = self.client.get('/features/compliance/')
        self.assertEqual(response.status_code, 200)

    def test_compliance_reversed_url(self):
        response = self.client.get(reverse('features:compliance'))
        self.assertEqual(response.status_code, 200)

    def test_support_url(self):
        response = self.client.get('/features/support/')
        self.assertEqual(response.status_code, 200)

    def test_support_reversed_url(self):
        response = self.client.get(reverse('features:support'))
        self.assertEqual(response.status_code, 200)

    def test_api_url(self):
        response = self.client.get('/features/api/')
        self.assertEqual(response.status_code, 200)

    def test_api_reversed_url(self):
        response = self.client.get(reverse('features:api'))
        self.assertEqual(response.status_code, 200)

    def test_merchant_url(self):
        response = self.client.get('/features/merchant/')
        self.assertEqual(response.status_code, 200)

    def test_merchant_reversed_url(self):
        response = self.client.get(reverse('features:merchant'))
        self.assertEqual(response.status_code, 200)
