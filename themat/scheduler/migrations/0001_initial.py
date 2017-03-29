# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('event_title', models.CharField(max_length=200)),
                ('begin_date', models.DateTimeField(verbose_name=b'begin date')),
                ('end_date', models.DateTimeField(verbose_name=b'end date')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('venue_name', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=200)),
                ('rating', models.IntegerField(default=50)),
                ('likes', models.IntegerField(default=0)),
                ('views', models.IntegerField(default=0)),
            ],
        ),
    ]
