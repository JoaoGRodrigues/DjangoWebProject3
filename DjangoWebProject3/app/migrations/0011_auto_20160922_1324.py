# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 12:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160922_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amos',
            name='exec_start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
