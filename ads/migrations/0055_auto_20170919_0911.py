# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 04:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0054_auto_20170911_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='commentAboutUs',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='investor',
            name='description',
            field=models.TextField(blank=True, max_length=700, null=True),
        ),
    ]
