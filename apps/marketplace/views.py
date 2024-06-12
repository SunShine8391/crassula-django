from django.views.generic import ListView, DetailView
from .models import App, Category
from apps.features.models import Feature


class MarketplaceListView(ListView):
    model = App
    template_name = 'marketplace/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class AppDetailView(DetailView):
    model = App
    template_name = 'marketplace/app.html'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'marketplace/category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['apps'] = App.objects.filter(categories=self.object)
        return context
