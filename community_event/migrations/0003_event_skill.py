# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 23:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20160313_1943'),
        ('community_event', '0002_auto_20160313_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='skill',
            field=models.ManyToManyField(to='user.Skill'),
        ),
    ]
