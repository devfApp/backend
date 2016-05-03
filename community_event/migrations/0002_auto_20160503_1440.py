# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-03 14:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
        ('community_event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='added_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='skill',
            field=models.ManyToManyField(blank=True, related_name='events', to='user.Skill'),
        ),
    ]