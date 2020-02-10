# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 07:03
from __future__ import unicode_literals

import ads.models
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0056_auto_20170919_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400, verbose_name='عنوان')),
                ('link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to=ads.models.Slide.SlideImage_directory_path, verbose_name='تصویر')),
                ('content', ckeditor.fields.RichTextField(verbose_name='متن')),
            ],
            options={
                'verbose_name': 'اسلاید',
                'verbose_name_plural': 'اسلایدها',
            },
        ),
    ]
