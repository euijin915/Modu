# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-17 01:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableau', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='filename',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
