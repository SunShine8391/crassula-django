from django.views.generic import TemplateView


class ChallengerBanksView(TemplateView):
    template_name = 'solutions/challenger_banks.html'


class RailsbankView(TemplateView):
    template_name = 'solutions/railsbank.html'


class ClearbankView(TemplateView):
    template_name = 'solutions/clearbank.html'
