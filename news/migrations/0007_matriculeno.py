# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150826_1922'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculeNo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('No', models.IntegerField(max_length=10)),
            ],
        ),
    ]
