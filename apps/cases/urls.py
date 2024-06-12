from django.urls import path
from . import views as view

app_name = 'cases'

urlpatterns = [
    path('paysend/', view.PaySendView.as_view(), name='paysend'),
    path('safe-currency/', view.SafeCurrencyView.as_view(),
         name='safe_currency'),
]
