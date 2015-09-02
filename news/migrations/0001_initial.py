# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import news.models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(verbose_name='password', blank=True, max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(verbose_name='Username', max_length=100)),
                ('email', models.EmailField(verbose_name='email address', unique=True, db_index=True, max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_name', models.CharField(blank=True, max_length=50)),
                ('first_name', models.CharField(blank=True, max_length=50)),
                ('joined', models.DateTimeField(null=True, auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', news.models.MyUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('article_title', models.CharField(max_length=500)),
                ('article_content', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('likes', models.BooleanField(default=False)),
                ('author', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='Images/%Y/%m/%d')),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MatriculeNo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('No', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='MatriculeNo',
            field=models.OneToOneField(blank=True, null=True, to='news.MatriculeNo'),
        ),
    ]
