# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-11 16:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdTime',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 11, 16, 37, 6, 905395)),
        ),
    ]
