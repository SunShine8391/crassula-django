from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'landings/home.html'


class CompanyView(TemplateView):
    template_name = 'landings/company.html'


class DevelopersView(TemplateView):
    template_name = 'landings/developers.html'


class ContactsView(TemplateView):
    template_name = 'landings/contacts.html'
