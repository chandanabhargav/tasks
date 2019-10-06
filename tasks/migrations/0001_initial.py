# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-08-31 02:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.TextField()),
                ('createdTime', models.DateTimeField()),
                ('completionDate', models.DateTimeField()),
                ('isDone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=50)),
                ('password', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.User'),
        ),
    ]
