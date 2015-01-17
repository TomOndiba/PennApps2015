# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0008_userprofile_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_link',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
