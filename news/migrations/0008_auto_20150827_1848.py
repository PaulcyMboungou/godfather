# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_matriculeno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matriculeno',
            name='No',
            field=models.IntegerField(),
        ),
    ]
