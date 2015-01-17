# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0006_auto_20150117_0850'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='comments',
            field=models.ForeignKey(blank=True, to='tindeers.Comment', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(default=b'E', max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='relationship_status',
            field=models.CharField(default=b'UN', max_length=100),
            preserve_default=True,
        ),
    ]
