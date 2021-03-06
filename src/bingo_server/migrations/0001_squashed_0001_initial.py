# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('bingo_server', '0001_initial')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='GameType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='PrimaryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='SecondaryCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Tile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('games', models.ManyToManyField(related_name='tiles', to='bingo_server.Game')),
                ('place', models.ManyToManyField(related_name='tiles', to='bingo_server.Place')),
                ('primary_categories', models.ManyToManyField(related_name='tiles', to='bingo_server.PrimaryCategory')),
                ('secondary_categories', models.ManyToManyField(related_name='tiles', to='bingo_server.SecondaryCategory')),
            ],
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='winnes', to='bingo_server.Game')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='bingo_server.GameType'),
        ),
        migrations.AddField(
            model_name='game',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='bingo_server.Place'),
        ),
        migrations.AddField(
            model_name='game',
            name='primary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='bingo_server.PrimaryCategory'),
        ),
        migrations.AddField(
            model_name='game',
            name='secondary_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games', to='bingo_server.SecondaryCategory'),
        ),
    ]
