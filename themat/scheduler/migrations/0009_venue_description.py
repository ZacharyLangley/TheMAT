# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0008_auto_20170401_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='venue',
            name='description',
            field=models.CharField(max_length=200, default=''),
            preserve_default=False,
        ),
    ]
