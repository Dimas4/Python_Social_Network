# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-30 17:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newmusic', '0004_auto_20180330_2030'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files_sv',
            name='users',
        ),
        migrations.AddField(
            model_name='files_sv',
            name='users',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='newmusic.Files'),
            preserve_default=False,
        ),
    ]
