# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20150827_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='MatriculeNo',
            field=models.OneToOneField(blank=True, to='news.MatriculeNo', null=True),
        ),
    ]
