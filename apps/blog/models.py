from django.db import models
from django.urls import reverse


class Post(models.Model):
    is_active = models.BooleanField(default=False)
    header = models.CharField(max_length=300, unique=True)
    image = models.ImageField(upload_to='blog/posts', null=True)
    slug = models.SlugField(max_length=320, unique=True)
    seo_title = models.CharField(max_length=200, unique=True)
    seo_description = models.TextField(max_length=300, unique=True)
    date_publish = models.DateField(auto_now_add=True)
    date_edit = models.DateField()
    text = models.TextField()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'posts'
        ordering = ['date_edit']

    def get_absolute_url(self):
        return reverse('blog:post', kwargs={'slug': self.slug})

    def __str__(self):
        return self.header
