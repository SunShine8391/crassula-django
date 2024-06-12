from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from apps.events.models import Event


class EventsURLTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_events_main_url(self):
        client = Client()
        response = client.get('/events/')
        self.assertEqual(response.status_code, 200)

    def test_events_main_reversed_url(self):
        response = self.client.get(reverse('events:list'))
        self.assertEqual(response.status_code, 200)

    def test_events_booking_success_url(self):
        client = Client()
        response = client.get('/events/booking/success/')
        self.assertEqual(response.status_code, 200)

    def test_events_booking_success_reversed_url(self):
        response = self.client.get(reverse('events:booking_success'))
        self.assertEqual(response.status_code, 200)


class EventDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='test_user', password='test_password'
        )
        self.client.login(username='test_user', password='test_password')
        self.event = Event.objects.create(
            promo_text='Test Event',
            name='Test Event',
            slug='test-event',
            status='upcoming',
            description='This is a test event',
            location='Test Location'
        )

    def test_event_detail_view(self):
        url = reverse('events:details', kwargs={'slug': self.event.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.promo_text)
        self.assertContains(response, self.event.description)
        self.assertContains(response, self.event.location)
        self.assertContains(response, self.event.slug)
