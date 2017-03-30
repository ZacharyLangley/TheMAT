from django.contrib import admin
from .models import Event, Venue
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event_title']}),
        ('Date information', {'fields': ['begin_date']}),
        ('Date Information', {'fields': ['end_date']}),
        ('Location', {'fields': ['location']}),
    ]
    list_display = ('event_title', 'begin_date', 'was_published_recently')
    list_filter = ['begin_date']
    search_fields = ['event_title']

admin.site.register(Event, EventAdmin)
admin.site.register(Venue)
