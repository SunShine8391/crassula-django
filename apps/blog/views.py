from django.views.generic import ListView, DetailView
from .models import Post


class BlogView(ListView):
    model = Post
    ordering = '-date_edit'
    template_name = 'blog/main.html'


class BlogPostView(DetailView):
    model = Post
    template_name = 'blog/post.html'
