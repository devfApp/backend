# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 19:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20160313_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='batch',
            field=models.CharField(blank=True, choices=[('6', 'batch 6'), ('8', 'batch 8'), ('1', 'batch 1'), ('5', 'batch 5'), ('10', 'batch 10'), ('2', 'batch 2'), ('4', 'batch 4'), ('3', 'batch 3'), ('9', 'batch 9'), ('7', 'batch 7')], max_length=10),
        ),
    ]
