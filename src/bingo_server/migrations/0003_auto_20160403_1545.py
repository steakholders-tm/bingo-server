# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 13:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bingo_server', '0002_auto_20160403_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tile',
            old_name='name',
            new_name='text',
        ),
    ]