# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_event_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='picture',
        ),
        migrations.AddField(
            model_name='event',
            name='img_url',
            field=models.URLField(default=''),
        ),
    ]
