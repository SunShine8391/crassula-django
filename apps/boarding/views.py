from django.views.generic import TemplateView


class RequestDemoView(TemplateView):
    template_name = 'boarding/request_demo.html'


class ThankYouView(TemplateView):
    template_name = 'boarding/thank_you.html'
