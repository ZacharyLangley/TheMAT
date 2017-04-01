# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0005_event_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
