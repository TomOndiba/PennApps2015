# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0005_auto_20150117_0849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='comments',
            field=models.ForeignKey(to='tindeers.Comment', null=True),
            preserve_default=True,
        ),
    ]
