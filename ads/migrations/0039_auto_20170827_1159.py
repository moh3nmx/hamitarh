# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 07:29
from __future__ import unicode_literals

import ads.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0038_auto_20170821_0054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='credits',
            field=models.CharField(blank=True, max_length=200, verbose_name='اعتبارات قانونی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='damage',
            field=models.CharField(blank=True, max_length=200, verbose_name='زیان\u200cدهی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='expected_gain',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='سود پیش\u200cبینی شده'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='expected_time',
            field=models.CharField(blank=True, max_length=5, null=True, verbose_name='زمان پیش\u200cبینی شده'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.State', verbose_name='استان'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='proposal',
            field=models.FileField(blank=True, upload_to=ads.models.Advertisement.AdFile_directory_path, verbose_name='پروپوزال'),
        ),
    ]
