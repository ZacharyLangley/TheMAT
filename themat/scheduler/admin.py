from django.contrib import admin
from .models import Event, Venue, UserProfile
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event_title']}),
        ('Date information', {'fields': ['begin_date']}),
        ('Date Information', {'fields': ['end_date']}),
        ('Location', {'fields': ['location']}),
        ('Image URL', {'fields': ['img_url']}),
        ('Description', {'fields': ['event_description']}),
    ]
    list_display = ('event_title', 'begin_date', 'location', 'was_published_recently')
    list_filter = ['begin_date']
    search_fields = ['event_title']

admin.site.register(Event, EventAdmin)
admin.site.register(Venue)
admin.site.register(UserProfile)
