# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150902_0202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(to='news.Comment'),
        ),
    ]
