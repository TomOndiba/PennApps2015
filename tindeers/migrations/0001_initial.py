# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('comment_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=120)),
                ('video_link', models.CharField(max_length=25)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('liked', models.BooleanField()),
                ('product', models.ForeignKey(to='tindeers.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('age', models.IntegerField(null=True)),
                ('location', models.CharField(max_length=255, blank=True)),
                ('gender', models.CharField(default=b'E', max_length=1, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'E', b'Eunuch')])),
                ('email', models.EmailField(max_length=75, blank=True)),
                ('relationship_status', models.CharField(default=b'UN', max_length=2, choices=[(b'UN', b'Unknown'), (b'SI', b'Single'), (b'RE', b'In a relationship'), (b'EN', b'Engaged'), (b'MA', b'Married'), (b'CI', b'In a civil union'), (b'DO', b'In a domestic partnership'), (b'OP', b'In an open relationship'), (b'CO', b"It's complicated"), (b'SE', b'Separated'), (b'DI', b'Divorced'), (b'WI', b'Widowed')])),
                ('comments', models.ForeignKey(to='tindeers.Comment')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='rating',
            name='rater',
            field=models.ForeignKey(to='tindeers.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='creator',
            field=models.ForeignKey(related_name='creator', to='tindeers.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='product',
            name='raters',
            field=models.ManyToManyField(related_name='raters', through='tindeers.Rating', to='tindeers.UserProfile'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='product',
            field=models.ForeignKey(to='tindeers.Product'),
            preserve_default=True,
        ),
    ]
