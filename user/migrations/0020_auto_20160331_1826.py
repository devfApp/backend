# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-31 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0019_auto_20160331_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='user_type',
            field=models.CharField(choices=[('alumni', 'alumni'), ('sensei', 'sensei'), ('admin', 'admin')], max_length=50),
        ),
    ]
