# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 05:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20170816_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_advertiser',
        ),
    ]
