# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20160313_1933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='user',
        ),
        migrations.AddField(
            model_name='myuser',
            name='skills',
            field=models.ManyToManyField(to='user.Skill'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='batch',
            field=models.CharField(blank=True, choices=[('1', 'batch 1'), ('7', 'batch 7'), ('10', 'batch 10'), ('5', 'batch 5'), ('8', 'batch 8'), ('3', 'batch 3'), ('4', 'batch 4'), ('2', 'batch 2'), ('9', 'batch 9'), ('6', 'batch 6')], max_length=10),
        ),
    ]
