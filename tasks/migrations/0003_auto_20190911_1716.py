# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-09-11 17:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20190911_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='createdTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
