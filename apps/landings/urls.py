from apps.landings import views as view
from django.urls import path

app_name = 'landings'

urlpatterns = [
    path('', view.HomeView.as_view(), name='home'),
    path('company/', view.CompanyView.as_view(), name='company'),
    path('developers/', view.DevelopersView.as_view(), name='developers'),
    path('contacts/', view.ContactsView.as_view(), name='contacts')
]
