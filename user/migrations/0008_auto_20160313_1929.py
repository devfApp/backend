# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 19:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20160313_1912'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Skills',
                'verbose_name': 'Skill',
            },
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='skills',
        ),
        migrations.AlterField(
            model_name='myuser',
            name='batch',
            field=models.CharField(blank=True, choices=[('8', 'batch 8'), ('7', 'batch 7'), ('3', 'batch 3'), ('6', 'batch 6'), ('4', 'batch 4'), ('2', 'batch 2'), ('1', 'batch 1'), ('9', 'batch 9'), ('5', 'batch 5'), ('10', 'batch 10')], max_length=10),
        ),
        migrations.AddField(
            model_name='skill',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='user.MyUser'),
        ),
    ]
