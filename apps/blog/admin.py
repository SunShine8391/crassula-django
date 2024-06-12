from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	save_as_continue = True
	list_display = ['id', 'header', 'is_active', 'date_edit']
	readonly_fields = ('id',)
