from django.urls import path
from apps.pages import views as view

app_name = 'pages'


urlpatterns = [
    path('privacy/', view.PrivacyView.as_view(), name='privacy'),
    path('terms/', view.TermsView.as_view(), name='terms'),
    path('gdpr/', view.GDPRView.as_view(), name='gdpr')
]
