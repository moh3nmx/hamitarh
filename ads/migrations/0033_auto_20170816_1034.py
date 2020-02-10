# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-16 10:34
from __future__ import unicode_literals

import ads.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0032_auto_20170815_2135'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=40, null=True, verbose_name='عنوان')),
                ('logo', models.ImageField(blank=True, upload_to=ads.models.Investor.InvestorLogo_directory_path, verbose_name='لوگو')),
                ('isBig', models.BooleanField(default=False, verbose_name='سرمایه گذار بزرگ')),
                ('interest', models.ManyToManyField(to='ads.AdCategory')),
            ],
        ),
        migrations.AddField(
            model_name='advertisement',
            name='investor',
            field=models.ManyToManyField(blank=True, null=True, to='ads.Investor', verbose_name='سرمایه گذار'),
        ),
    ]
