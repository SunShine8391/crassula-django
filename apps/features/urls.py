from django.urls import path
from apps.features import views as view

app_name = 'features'

urlpatterns = [
    path('cards/', view.Cards.as_view(), name='cards'),
    path('prices/', view.Prices.as_view(), name='prices'),
    path('accounts/', view.Accounts.as_view(), name='accounts'),
    path('transfers/', view.Transfers.as_view(), name='transfers'),
    path('currency-exchange/', view.CurrencyExchange.as_view(),
         name='currency_exchange'),
    path('crypto/', view.Crypto.as_view(), name='crypto'),
    path('dashboard/', view.Dashboard.as_view(), name='dashboard'),
    path('ui/', view.UI.as_view(), name='ui'),
    path('compliance/', view.Compliance.as_view(), name='compliance'),
    path('support/', view.Support.as_view(), name='support'),
    path('api/', view.API.as_view(), name='api'),
    path('merchant/', view.Merchant.as_view(), name='merchant'),
]
