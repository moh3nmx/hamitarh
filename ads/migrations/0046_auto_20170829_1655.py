# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 12:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0045_auto_20170829_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='estimatedCosts',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='هزینه های پیش بینی شده'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='executiveSummary',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='خلاصه اجرایی طرح'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='fundUsage',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='نحوه استفاده از سرمایه جذب شده'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='investorShare',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='درصد مشارکت سرمایه گذار'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='presentIncome',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='وضعیت فعلی درآمد'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='resume',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='سابقه کاری'),
        ),
        migrations.AlterField(
            model_name='advertisement',
            name='revenueModel',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='مدل درآمدی'),
        ),
    ]
