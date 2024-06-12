from django.views.generic import TemplateView


class PrivacyView(TemplateView):
    template_name = 'pages/privacy.html'


class TermsView(TemplateView):
    template_name = 'pages/terms.html'


class GDPRView(TemplateView):
    template_name = 'pages/gdpr.html'
