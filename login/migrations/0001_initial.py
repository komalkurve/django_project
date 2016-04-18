# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-14 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Twit',
            fields=[
                ('keyword', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('freq', models.IntegerField()),
                ('num', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Twitlocation',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('keyword', models.CharField(max_length=100)),
                ('freq', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Twittime',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('keyword', models.CharField(max_length=100)),
                ('freq', models.IntegerField()),
            ],
        ),
    ]