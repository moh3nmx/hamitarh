# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-07 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20170807_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='fundingStep',
            field=models.CharField(blank=True, choices=[('0', 'نقد و بررسی فنی'), ('1', 'جلسه ارزیابی اقتصادی'), ('2', 'معرفی به سرمایه گذار'), ('3', 'عقد قرارداد')], max_length=30, verbose_name='Step'),
        ),
    ]
