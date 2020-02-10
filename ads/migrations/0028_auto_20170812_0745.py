# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0027_auto_20170809_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='fundingStep',
            field=models.CharField(blank=True, choices=[('0', 'نقد و بررسی'), ('1', 'جلسه حضوری'), ('2', 'معرفی به سرمایه گذار'), ('3', 'عقد قرارداد')], max_length=30, null=True, verbose_name='آخرین درخواست'),
        ),
    ]
