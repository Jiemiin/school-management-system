# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-19 21:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20170915_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='daily_attendance',
            name='section',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='home.Sections'),
        ),
    ]
