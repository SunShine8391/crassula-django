from django.urls import path
from django.contrib.sitemaps.views import sitemap

from .views import (
    RobotsView, GuidesViewSitemap, BlogViewSitemap, SitemapView
)

app_name = 'seo'

sitemap_default = {
    'sitemap': SitemapView
}

sitemap_guides = {
    'guides': GuidesViewSitemap
}

sitemap_blog = {
    'posts': BlogViewSitemap
}

urlpatterns = [
    path('robots.txt', RobotsView.as_view()),
    path(
        'sitemap.xml',
        sitemap, {'sitemaps': sitemap_default},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'sitemap_guides.xml',
        sitemap, {'sitemaps': sitemap_guides},
        name='django.contrib.sitemaps.views.sitemap'
    ),
    path(
        'sitemap_blog.xml',
        sitemap, {'sitemaps': sitemap_blog},
        name='django.contrib.sitemaps.views.sitemap'
    ),
]
