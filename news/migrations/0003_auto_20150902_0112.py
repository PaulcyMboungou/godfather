# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150829_0019'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ForeignKey(null=True, blank=True, to='news.Comment'),
        ),
    ]
