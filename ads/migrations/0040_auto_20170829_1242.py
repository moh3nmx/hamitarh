# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0039_auto_20170827_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertisement',
            name='address',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='commentCount',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='inv_deadline',
        ),
        migrations.RemoveField(
            model_name='advertisement',
            name='isFree',
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ثبت'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='lastModified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
