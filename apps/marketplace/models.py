from django.db import models
from django.urls import reverse

from apps.features.models import Feature


class Category(models.Model):
    is_active = models.BooleanField(default=True)
    name = models.CharField(max_length=20, unique=True)
    slug = models.SlugField(max_length=30, unique=True)
    seo_title = models.CharField(max_length=180, unique=True)
    seo_description = models.TextField(max_length=300, unique=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('marketplace:category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name


class App(models.Model):
    is_active = models.BooleanField(default=True)
    logo = models.ImageField(
        upload_to='marketplace/app/logo', blank=True, null=True
    )
    details_logo = models.ImageField(
        upload_to='marketplace/app/logo', blank=True, null=True
    )
    name = models.CharField(max_length=20, unique=True)
    header = models.CharField(
        max_length=30, blank=True, null=True,
        verbose_name='Header (75 characters)'
    )
    slug = models.SlugField(max_length=30, unique=True)

    # SEO
    seo_title = models.CharField(max_length=180, unique=True)
    seo_description = models.TextField(max_length=300, unique=True)

    # Info
    small_description = models.TextField(
        max_length=75, verbose_name='Small description (75 characters)'
    )
    full_description = models.TextField(max_length=1000)
    categories = models.ManyToManyField(Category)
    features = models.ManyToManyField(Feature, blank=True)

    # Resources
    website_url = models.URLField(blank=True, null=True)
    support_url = models.URLField(blank=True, null=True)
    faq_url = models.URLField(blank=True, null=True)

    # Screens
    show_screens = models.BooleanField(default=False)
    screen_1 = models.ImageField(
        upload_to='marketplace/app/screen', blank=True, null=True
    )
    screen_2 = models.ImageField(
        upload_to='marketplace/app/screen', blank=True, null=True
    )
    screen_3 = models.ImageField(
        upload_to='marketplace/app/screen', blank=True, null=True
    )
    screen_4 = models.ImageField(
        upload_to='marketplace/app/screen', blank=True, null=True
    )
    screen_5 = models.ImageField(
        upload_to='marketplace/app/screen', blank=True, null=True
    )

    def get_absolute_url(self):
        return reverse('marketplace:app', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name
