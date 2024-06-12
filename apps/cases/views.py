from django.views.generic import TemplateView


class SafeCurrencyView(TemplateView):
    template_name = 'cases/safe_currency.html'


class PaySendView(TemplateView):
    template_name = 'cases/paysend.html'
