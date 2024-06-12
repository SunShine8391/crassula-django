from django.contrib import admin
from .models import Guide, FAQ, SubContent

@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'content', 'published_date', 'modified_date')
    list_filter = ('title', 'published_date')
    search_fields = ('title', 'description', 'content')


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'guide_id')
    list_filter = ('question', 'answer')
    search_fields = ('question', 'answer')

@admin.register(SubContent)
class SubContentAdmin(admin.ModelAdmin):
    list_display = ('sub_title', 'sub_content', 'sub_guide')
    list_filter = ('sub_title', 'sub_content')
    search_fields = ('sub_title', 'sub_content')
