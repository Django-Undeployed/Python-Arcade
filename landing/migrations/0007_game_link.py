# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-02 17:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0006_auto_20161102_0154'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='link',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]
