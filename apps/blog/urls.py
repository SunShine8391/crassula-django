from django.urls import path
from .views import BlogView, BlogPostView

app_name = 'blog'

urlpatterns = [
    path('', BlogView.as_view(), name='main'),
    path('<slug:slug>/', BlogPostView.as_view(), name='post')
]
