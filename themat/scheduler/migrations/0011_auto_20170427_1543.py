# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0010_auto_20170426_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_venue',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.ForeignKey(to='scheduler.Venue', null=True),
        ),
    ]
