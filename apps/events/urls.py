from .views import EventListView, EventDetailView, EventBookingSuccessView
from django.urls import path

app_name = 'events'

urlpatterns = [
    path('', EventListView.as_view(), name='list'),
    path('<slug:slug>/', EventDetailView.as_view(), name='details'),
    path('booking/success/', EventBookingSuccessView.as_view(),
         name='booking_success'),
]
