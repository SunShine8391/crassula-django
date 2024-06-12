from django.db import models
from django.urls import reverse

class Guide(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(null=True)
    content = models.TextField(null=True)
    published_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(null=True)
   
    class Meta:
        verbose_name = 'Guide'
        verbose_name_plural = 'Guide'
        ordering = ('-published_date',)

    def get_absolute_url(self):
        return reverse('guides:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255, blank=True, null=True)
    answer = models.TextField()
    guide_id = models.ForeignKey(Guide, on_delete=models.CASCADE)
   
    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ' 
        ordering = ('id',)

    def __str__(self):
        return self.question

class SubContent(models.Model):
    sub_title = models.TextField(null=True)
    sub_content = models.TextField(null=True)
    sub_guide = models.ForeignKey(Guide, on_delete=models.CASCADE) 
    call = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'SubContent'
        verbose_name_plural = 'SubContent'
        ordering = ('id',)

    def __str__(self):
        return self.sub_title