from django.db import models

# Create your models here.
class Event(models.Model):
    event_title = models.CharField(max_length=200)
    begin_date = models.DateTimeField('begin date')
    end_date = models.DateTimeField('end date')
    location = models.CharField(max_length=200)

    def __unicode__(self):
        return self.event_title

    def was_published_recently(self):
        return self.end_date >= timezone.now() - datetime.timedelta(days=1)

class Venue(models.Model):
    venue_name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    rating = models.IntegerField(default=50)
    likes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)

    def __unicode__(self):
        return self.venue_name
