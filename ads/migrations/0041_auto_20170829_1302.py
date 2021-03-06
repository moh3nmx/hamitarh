# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 08:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0040_auto_20170829_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='estimatedCosts',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='هزینه های پیش بینی شده'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='executiveSummary',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='خلاصه اجرایی طرح'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='fundUsage',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='نحوه استفاده از سرمایه جذب شده'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='investorShare',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='درصد مشارکت سرمایه گذار'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='presentIncome',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='وضعیت فعلی درآمد'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='resume',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='سابقه کاری'),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='revenueModel',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='مدل درآمدی'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='credits',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='نحوه ضمانت'),
        ),
    ]
