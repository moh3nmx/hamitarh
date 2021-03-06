# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0055_auto_20170919_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='commentAboutUs',
            field=models.TextField(blank=True, max_length=700, null=True, verbose_name='پیام برای حامی طرح'),
        ),
        migrations.AlterField(
            model_name='investor',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='کشور'),
        ),
        migrations.AlterField(
            model_name='investor',
            name='description',
            field=models.TextField(blank=True, max_length=700, null=True, verbose_name='درباره سرمایه گذار'),
        ),
    ]
