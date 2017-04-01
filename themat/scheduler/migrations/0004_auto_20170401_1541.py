# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_description',
            field=models.CharField(max_length=1000, default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to='profile_images', blank=True),
        ),
    ]
