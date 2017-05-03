import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Venue(models.Model):
    venue_name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    rating = models.IntegerField(default=50)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    img_url = models.URLField(max_length=200, default="")
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.venue_name

    def __str__(self):
        return self.venue_name

    def get_absolute_url(self):
        return '/venue/' + str(self.id)

class Event(models.Model):
    event_title = models.CharField(max_length=200)
    begin_date = models.DateTimeField('begin date')
    end_date = models.DateTimeField('end date')
    location = models.ForeignKey(Venue, on_delete=models.CASCADE)
    event_description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    img_url = models.URLField(max_length=1000, default="")

    def __unicode__(self):
        return self.event_title

    def __str__(self):
        return self.event_title

    #Used to go back to event after updating
    def get_absolute_url(self):
        return '/event/' + str(self.id)

    def was_published_recently(self):
        return self.end_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'begin_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Recently Published'

class AttendEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username + ' ' + self.event.event_title

    def __str__(self):
        return self.user.username + ' ' + self.event.event_title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.FileField()
    is_venue = models.BooleanField(default=False)
    location = models.ForeignKey(Venue, null=True, blank=True)


    def __unicode__(self):
        return self.user.username

    def __str__(self):
        return self.user.username

class LikedVenue(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user.username + ' ' + self.venue.venue_name

    def __str__(self):
        return self.user.username + ' ' + self.venue.venue_name
