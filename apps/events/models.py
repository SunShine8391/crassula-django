from django.db import models
from django.urls import reverse


class Event(models.Model):
    EVENT_STATUS = [
        ('live', 'Live'),
        ('ended', 'Ended'),
        ('upcoming', 'Upcoming')
    ]

    is_active = models.BooleanField(default=False)
    promote = models.BooleanField(default=False)
    status = models.CharField(choices=EVENT_STATUS, max_length=100)
    name = models.CharField(max_length=50, blank=True, null=True)
    promo_text = models.CharField(max_length=255)
    slug = models.SlugField()
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=100, blank=True, null=True)
    stand = models.CharField(max_length=255, blank=True, null=True)
    logo = models.ImageField(upload_to='events')
    about_top = models.TextField(blank=True, null=True)
    image_1 = models.ImageField(upload_to='events', blank=True, null=True)
    image_2 = models.ImageField(upload_to='events', blank=True, null=True)
    about_bottom = models.TextField(blank=True, null=True)
    members = models.ManyToManyField('Member', blank=True)

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
        ordering = ('-date_start',)

    def get_absolute_url(self):
        return reverse('events:details', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class Booking(models.Model):
    done = models.BooleanField(default=False)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    description = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Booking'
        verbose_name_plural = 'Bookings'
        ordering = ('-date',)

    def __str__(self):
        return self.email


class Member(models.Model):
    full_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='members')

    class Meta:
        verbose_name = 'Member'
        verbose_name_plural = 'Members'
        ordering = ('full_name',)

    def __str__(self):
        return self.full_name
