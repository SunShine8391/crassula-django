from django.contrib import admin
from .models import Event, Booking, Member


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'date_start', 'date_end', 'status', 'is_active', 'promote'
    )
    list_filter = ('status', 'promote')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'done', 'email', 'phone', 'date', 'event')
    list_filter = ('event', 'done')
    search_fields = ('name', 'email', 'phone', 'description')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'title')
