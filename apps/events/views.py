from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from .forms import BookingForm
from .models import Event, Booking


class EventListView(ListView):
    model = Event
    template_name = 'events/list.html'
    context_object_name = 'events'
    queryset = Event.objects.filter(is_active=True)


class EventDetailView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'events/details.html'
    success_url = reverse_lazy('events:booking_success')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(slug=self.kwargs['slug'])
        return context

    def form_valid(self, form):
        form.instance.event = Event.objects.get(slug=self.kwargs['slug'])
        return super().form_valid(form)


class EventBookingSuccessView(TemplateView):
    template_name = 'events/booking_success.html'
