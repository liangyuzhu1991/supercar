# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-05 19:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('race', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='pub_date',
        ),
    ]
