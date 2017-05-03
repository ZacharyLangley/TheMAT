# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0011_auto_20170427_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='venue',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
