from django.urls import path
from . import views as view

app_name = 'solutions'

urlpatterns = [
    path('clearbank/', view.ClearbankView.as_view(), name='clearbank'),
    path('challenger-banks/', view.ChallengerBanksView.as_view(),
         name='challenger_banks'),
    path('railsr/', view.RailsbankView.as_view(), name='railsr'),
]
