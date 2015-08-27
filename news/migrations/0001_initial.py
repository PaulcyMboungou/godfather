# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', null=True, blank=True)),
                ('email', models.EmailField(unique=True, verbose_name='email address', db_index=True, max_length=254)),
                ('joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('article_title', models.CharField(max_length=500)),
                ('article_content', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('likes', models.BooleanField(default=False)),
                ('author', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(upload_to='Images/%Y/%m/%d', blank=True)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
    ]
