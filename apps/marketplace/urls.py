from django.urls import path
from apps.marketplace import views as view


app_name = 'marketplace'

urlpatterns = [
    path('', view.MarketplaceListView.as_view(), name='main'),
    path('app/<slug:slug>/', view.AppDetailView.as_view(), name='app'),
    path('category/<slug:slug>/', view.CategoryDetailView.as_view(), name='category'),
]
