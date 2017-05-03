# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0012_auto_20170430_2242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='img_url',
            field=models.URLField(default='', max_length=1000),
        ),
    ]
