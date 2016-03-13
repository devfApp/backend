# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 19:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20160312_0334'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='work',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '55-5555-5555'. Up to 15 digits allowed.", regex='^\\+?1?\\d{10,15}$')]),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='profile_pic/'),
        ),
    ]