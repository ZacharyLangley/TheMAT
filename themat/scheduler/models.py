import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=200)
    begin_date = models.DateTimeField('begin date')
    end_date = models.DateTimeField('end date')
    location = models.CharField(max_length=200)
    event_description = models.CharField(max_length=1000)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    img_url = models.URLField(max_length=200, default="")

    def __unicode__(self):
        return self.event_title

    def was_published_recently(self):
        return self.end_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'begin_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Recently Published'


class Venue(models.Model):
    venue_name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    rating = models.IntegerField(default=50)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    img_url = models.URLField(max_length=200, default="")

    def __unicode__(self):
        return self.venue_name

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __unicode__(self):
        return self.user.username
