# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 12:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bingo_server', '0001_squashed_0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date',
            field=models.DateField(default=datetime.date(2016, 4, 3)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='game',
            name='time',
            field=models.TimeField(default=datetime.time(12, 38, 25, 688617)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='winner',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 3, 12, 38, 35, 635179, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='game',
            name='secondary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='games', to='bingo_server.SecondaryCategory'),
        ),
        migrations.AlterField(
            model_name='gametype',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='primarycategory',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='secondarycategory',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='tile',
            name='games',
            field=models.ManyToManyField(blank=True, related_name='tiles', to='bingo_server.Game'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='place',
            field=models.ManyToManyField(blank=True, related_name='tiles', to='bingo_server.Place'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='primary_categories',
            field=models.ManyToManyField(blank=True, related_name='tiles', to='bingo_server.PrimaryCategory'),
        ),
        migrations.AlterField(
            model_name='tile',
            name='secondary_categories',
            field=models.ManyToManyField(blank=True, related_name='tiles', to='bingo_server.SecondaryCategory'),
        ),
        migrations.AlterField(
            model_name='winner',
            name='game',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winners', to='bingo_server.Game'),
        ),
    ]
