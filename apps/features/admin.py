from django.contrib import admin
from .models import Feature

@admin.register(Feature)
class PostAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	save_as_continue = True
	list_display = ['id', 'name', 'url']
	readonly_fields = ('id',)
