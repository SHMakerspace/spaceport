# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-20 22:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('access', '0004_auto_20171220_1736'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesslog',
            name='Node',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='access.SecurityNode'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accesslog',
            name='Out',
            field=models.DateTimeField(blank=True),
        ),
    ]