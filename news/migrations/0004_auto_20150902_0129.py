# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20150902_0112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='comment',
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(to='news.Comment', blank=True, null=True),
        ),
    ]
