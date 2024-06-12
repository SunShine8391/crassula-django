from django.urls import path
from .views import CareerView

app_name = 'careers'

urlpatterns = [
    path('careers/', CareerView.as_view(), name='main')
]
