# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 07:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_advertisement_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ads.State'),
        ),
    ]