# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0034_auto_20170816_1107'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='investor',
            options={'verbose_name': 'سرمایه گذار', 'verbose_name_plural': 'سرمایه گذاران'},
        ),
    ]