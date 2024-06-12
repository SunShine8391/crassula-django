from django.views.generic.base import TemplateView
from django.contrib.sitemaps import Sitemap
from apps.blog.models import Post


class RobotsView(TemplateView):
    template_name = 'seo/robots.txt'
    content_type = 'text/plain'


class SitemapView(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            '/',
            '/features/cards/',
            '/features/prices/',
            '/features/accounts/',
            '/features/transfers/',
            '/features/currency-exchange/',
            '/features/crypto/',
            '/features/dashboard/',
            '/features/ui/',
            '/features/compliance/',
            '/features/support/',
            '/features/api/',
            '/features/merchant/',
            '/solutions/challenger-banks/',
            '/solutions/railsr/',
            '/solutions/clearbank/',
            '/developers/',
            '/blog/',
            '/company/',
            '/contacts/',
            '/careers/',
            '/privacy/',
            '/terms/',
            '/gdpr/',
            '/cases/paysend/',
            '/cases/safe-currency/',
        ]

    def location(self, obj):
        return obj

class BlogViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(is_active=True)


class GuidesViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.5

    def items(self):
        return [
            '/guides/',
            '/guides/core-banking/',
            '/guides/banking-as-a-service/',
            '/guides/white-label-payment-gateway/',
            '/guides/digital-banking/',
            '/guides/banking-software/',
            '/guides/crypto-exchange-software/',
            '/guides/open-banking/',
            '/guides/white-label-credit-cards/',
            '/guides/white-label-debit-cards/',
            '/guides/white-label-crypto-wallet/',
            '/guides/baas-providers/',
            '/guides/cryptocurrency-exchange/',
            '/guides/white-label-digital-wallet/',
            '/merchant-management-software/',
            '/guides/white-label-mobile-banking/',
        ]

    def location(self, obj):
        return obj

