# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-18 19:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0005_auto_20190518_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='race_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 18, 19, 19, 4, 549415, tzinfo=utc), verbose_name='race date'),
        ),
    ]
