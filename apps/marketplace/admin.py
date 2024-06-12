from django.contrib import admin
from .models import App, Category

@admin.register(App)
class PostAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	save_as_continue = True
	list_display = ['id', 'name', 'header', 'is_active']
	readonly_fields = ('id',)

@admin.register(Category)
class PostAdmin(admin.ModelAdmin):
	save_as = True
	save_on_top = True
	save_as_continue = True
	list_display = ['id', 'name', 'is_active']
	readonly_fields = ('id',)
