# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 22:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sensei_stuff', '0008_auto_20160316_2232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='challenge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensei_stuff.Challenge'),
        ),
    ]
