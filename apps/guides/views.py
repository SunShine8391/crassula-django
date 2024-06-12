from django.views.generic import TemplateView, ListView, DetailView
from .models import Guide, FAQ, SubContent

class GuideListView(ListView):
    model = Guide
    template_name = 'guides/main.html'

class GuideDetailListView(DetailView):
    model = Guide
    template_name = 'guides/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['FAQ'] = FAQ.objects.filter(guide_id=self.kwargs['pk'])
        context['SubContent'] = SubContent.objects.filter(sub_guide_id=self.kwargs['pk'])
        return context
