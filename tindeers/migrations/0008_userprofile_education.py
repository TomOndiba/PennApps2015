# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0007_auto_20150117_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(default=b'E', max_length=20),
            preserve_default=True,
        ),
    ]
