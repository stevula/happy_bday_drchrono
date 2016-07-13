# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-13 06:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_auto_20160713_0531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='greeting',
            name='dob',
        ),
        migrations.AddField(
            model_name='greeting',
            name='birth_day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='greeting',
            name='birth_month',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
