# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-20 03:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('access_token', models.CharField(max_length=50)),
                ('refresh_token', models.CharField(max_length=50)),
                ('expires_timestamp', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Greeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('birth_day', models.IntegerField(blank=True, null=True)),
                ('birth_month', models.IntegerField(blank=True, null=True)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
