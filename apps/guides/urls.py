from django.urls import path
from apps.guides import views as view
from .views import GuideListView, GuideDetailListView

app_name = 'guides'

urlpatterns = [
    path('', GuideListView.as_view(), name='main'),
    path('<int:pk>/', GuideDetailListView.as_view(), name='detail'),
]
