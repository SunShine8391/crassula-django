from django.test import Client, TestCase
from django.urls import reverse


class GuidesURLTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_guides_main_url(self):
        response = self.client.get('/guides/')
        self.assertEqual(response.status_code, 200)

    def test_guides_main_reversed_url(self):
        response = self.client.get(reverse('guides:main'))
        self.assertEqual(response.status_code, 200)

    def test_core_banking_main_url(self):
        response = self.client.get('/guides/core-banking/')
        self.assertEqual(response.status_code, 200)

    def test_core_banking_reversed_url(self):
        response = self.client.get(reverse('guides:core_banking'))
        self.assertEqual(response.status_code, 200)

    def test_banking_as_a_service_main_url(self):
        response = self.client.get('/guides/banking-as-a-service/')
        self.assertEqual(response.status_code, 200)

    def test_banking_as_a_service_reversed_url(self):
        response = self.client.get(reverse('guides:banking_as_a_service'))
        self.assertEqual(response.status_code, 200)

    def test_baas_providers_main_url(self):
        response = self.client.get('/guides/baas-providers/')
        self.assertEqual(response.status_code, 200)

    def test_baas_providers_reversed_url(self):
        response = self.client.get(reverse('guides:baas_providers'))
        self.assertEqual(response.status_code, 200)

    def test_white_label_payment_gateway_main_url(self):
        response = self.client.get('/guides/white-label-payment-gateway/')
        self.assertEqual(response.status_code, 200)

    def test_white_label_payment_gateway_reversed_url(self):
        response = self.client.get(
            reverse('guides:white_label_payment_gateway')
        )
        self.assertEqual(response.status_code, 200)

    def test_digital_banking_main_url(self):
        response = self.client.get('/guides/digital-banking/')
        self.assertEqual(response.status_code, 200)

    def test_digital_banking_reversed_url(self):
        response = self.client.get(reverse('guides:digital_banking'))
        self.assertEqual(response.status_code, 200)

    def test_banking_software_main_url(self):
        response = self.client.get('/guides/banking-software/')
        self.assertEqual(response.status_code, 200)

    def test_banking_software_reversed_url(self):
        response = self.client.get(reverse('guides:banking_software'))
        self.assertEqual(response.status_code, 200)

    def test_crypto_exchange_software_main_url(self):
        response = self.client.get('/guides/crypto-exchange-software/')
        self.assertEqual(response.status_code, 200)

    def test_crypto_exchange_software_reversed_url(self):
        response = self.client.get(reverse('guides:crypto_exchange_software'))
        self.assertEqual(response.status_code, 200)

    def test_open_banking_main_url(self):
        response = self.client.get('/guides/open-banking/')
        self.assertEqual(response.status_code, 200)

    def test_open_banking_reversed_url(self):
        response = self.client.get(reverse('guides:open_banking'))
        self.assertEqual(response.status_code, 200)

    def test_white_label_debit_cards_main_url(self):
        response = self.client.get('/guides/white-label-debit-cards/')
        self.assertEqual(response.status_code, 200)

    def test_white_label_debit_cards_reversed_url(self):
        response = self.client.get(reverse('guides:wl_debit_card'))
        self.assertEqual(response.status_code, 200)

    def test_white_label_credit_cards_main_url(self):
        response = self.client.get('/guides/white-label-credit-cards/')
        self.assertEqual(response.status_code, 200)

    def test_white_label_credit_cards_reversed_url(self):
        response = self.client.get(reverse('guides:wl_credit_card'))
        self.assertEqual(response.status_code, 200)

    def test_white_label_crypto_wallet_main_url(self):
        response = self.client.get('/guides/white-label-crypto-wallet/')
        self.assertEqual(response.status_code, 200)

    def test_white_label_crypto_wallet_reversed_url(self):
        response = self.client.get(reverse('guides:wl_crypto_wallet'))
        self.assertEqual(response.status_code, 200)

    def test_cryptocurrency_exchange_main_url(self):
        response = self.client.get('/guides/cryptocurrency-exchange/')
        self.assertEqual(response.status_code, 200)

    def test_cryptocurrency_exchange_reversed_url(self):
        response = self.client.get(
            reverse('guides:build_cryptocurrency_exchange')
        )
        self.assertEqual(response.status_code, 200)

    def test_white_label_digital_wallet_main_url(self):
        response = self.client.get('/guides/white-label-digital-wallet/')
        self.assertEqual(response.status_code, 200)

    def test_white_label_digital_wallet_reversed_url(self):
        response = self.client.get(reverse('guides:wl_digital_wallet'))
        self.assertEqual(response.status_code, 200)

    def test_merchant_management_software_main_url(self):
        response = self.client.get('/guides/merchant-management-software/')
        self.assertEqual(response.status_code, 200)

    def test_merchant_management_software_reversed_url(self):
        response = self.client.get(
            reverse('guides:merchant_management_software')
        )
        self.assertEqual(response.status_code, 200)

    def test_white_label_mobile_banking_main_url(self):
        response = self.client.get('/guides/white-label-mobile-banking/')
        self.assertEqual(response.status_code, 200)

    def test_white_label_mobile_banking_reversed_url(self):
        response = self.client.get(reverse('guides:wl_mobile_banking'))
        self.assertEqual(response.status_code, 200)
