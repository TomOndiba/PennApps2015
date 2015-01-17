# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0004_auto_20150117_0425'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='email',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'E', max_length=1, choices=[(b'M', b'male'), (b'F', b'female'), (b'E', b'Eunuch')]),
            preserve_default=True,
        ),
    ]
