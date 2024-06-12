from django.urls import path
from .views import RequestDemoView, ThankYouView

app_name = 'boarding'

urlpatterns = [
    path('request-demo/', RequestDemoView.as_view(), name='request_demo'),
    path('thankyou/', ThankYouView.as_view(), name='thankyou')
]
