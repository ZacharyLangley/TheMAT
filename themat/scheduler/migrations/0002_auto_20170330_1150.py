# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='img_url',
            field=models.URLField(default=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='begin_date',
            field=models.DateTimeField(verbose_name='begin date'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(verbose_name='end date'),
        ),
    ]
