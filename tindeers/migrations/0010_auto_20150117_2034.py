# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tindeers', '0009_product_product_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(max_length=200),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(related_name='my_products', to='tindeers.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=160),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='product',
            name='raters',
            field=models.ManyToManyField(related_name='my_rated_products', through='tindeers.Rating', to='tindeers.UserProfile'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.CharField(default=b'High School', max_length=20),
            preserve_default=True,
        ),
    ]
