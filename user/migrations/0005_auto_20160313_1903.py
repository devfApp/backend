# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20160313_1901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='work',
            new_name='job',
        ),
    ]
