# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 05:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0053_investor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investor',
            name='interest',
            field=models.ManyToManyField(to='ads.AdCategory', verbose_name='علاقه مندی ها'),
        ),
    ]
