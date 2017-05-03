from django.contrib import admin
from .models import Event, Venue, UserProfile, AttendEvent
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

class UserProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Website', {'fields': ['website']}),
        ('Is Venue', {'fields': ['is_venue']}),
        ('Location', {'fields': ['location']}),
        ('picture', {'fields': ['picture']}),
    ]
    list_display = ('user', 'website', 'is_venue', 'location')
    list_filter = ['location']
    search_fields = ['user']

class VenueAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['venue_name']}),
        ('Location', {'fields': ['location']}),
        ('Rating', {'fields': ['rating']}),
        ('Likes', {'fields': ['likes']}),
        ('Views', {'fields': ['views']}),
        ('Image URL', {'fields': ['img_url']}),
        ('Description', {'fields': ['description']}),

        ]
    list_display = ('venue_name', 'location', 'rating', 'likes', 'views')
    search_fields = ['venue_name']

class AttendEventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user']}),
        ('Event', {'fields': ['event']}),
        ]
    list_display = ('user', 'event')
    list_filter = ['user', 'event']
    search_fields = ['event']

admin.site.register(Event, EventAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(AttendEvent, AttendEventAdmin)
