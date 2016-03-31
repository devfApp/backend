# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20160315_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('1', 'alumni'), ('2', 'sensei'), ('3', 'admin')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
