# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.CharField(default=1, max_length=8),
            preserve_default=False,
        ),
    ]