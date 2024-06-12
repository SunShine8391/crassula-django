from django.views.generic import TemplateView


class Cards(TemplateView):
    template_name = 'features/cards.html'


class Prices(TemplateView):
    template_name = 'features/prices.html'


class Accounts(TemplateView):
    template_name = 'features/accounts.html'


class Transfers(TemplateView):
    template_name = 'features/transfers.html'


class CurrencyExchange(TemplateView):
    template_name = 'features/currency-exchange.html'


class Crypto(TemplateView):
    template_name = 'features/crypto.html'


class Dashboard(TemplateView):
    template_name = 'features/dashboard.html'


class UI(TemplateView):
    template_name = 'features/ui.html'


class Compliance(TemplateView):
    template_name = 'features/compliance.html'


class Support(TemplateView):
    template_name = 'features/support.html'


class API(TemplateView):
    template_name = 'features/api.html'


class Merchant(TemplateView):
    template_name = 'features/merchant.html'
