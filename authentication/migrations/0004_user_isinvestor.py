# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 05:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_remove_user_is_advertiser'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='isInvestor',
            field=models.BooleanField(default=False, verbose_name='نماینده سرمایه گذار'),
        ),
    ]