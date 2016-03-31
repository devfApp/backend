# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-15 20:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0016_auto_20160315_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('sensei', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.MyUser')),
            ],
            options={
                'verbose_name': 'Challenge',
                'verbose_name_plural': 'Challenges',
            },
        ),
    ]
