# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0003_comment_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video_link',
            field=models.CharField(max_length=100),
            preserve_default=True,
        ),
    ]
