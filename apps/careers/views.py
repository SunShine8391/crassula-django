from django.views.generic import TemplateView


class CareerView(TemplateView):
    template_name = 'careers/main.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = None
        return context
