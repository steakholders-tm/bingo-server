#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import DateField, TimeField, CharField, Model, ManyToManyField, IntegerField, ForeignKey, DateTimeField


# Create your models here.
class Game(Model):
    name = CharField(max_length=256)
    date = DateField()
    time = TimeField()
    duration = IntegerField()
    game_type = ForeignKey(to="GameType", related_name="games")
    place = ForeignKey(to="Place", related_name="games")
    primary_category = ForeignKey(to="PrimaryCategory", related_name="games")
    secondary_category = ForeignKey(null=True, blank=True, to="SecondaryCategory", related_name="games")


class GameType(Model):
    name = CharField(max_length=256)
    description = CharField(blank=True, max_length=512)


class Place(Model):
    name = CharField(max_length=256)
    description = CharField(blank=True, max_length=512)


class PrimaryCategory(Model):
    name = CharField(max_length=256)
    description = CharField(blank=True, max_length=512)


class SecondaryCategory(Model):
    name = CharField(max_length=256)
    description = CharField(blank=True, max_length=512)


class Tile(Model):
    text = CharField(max_length=256)
    games = ManyToManyField(blank=True, to="Game", related_name="tiles")
    place = ManyToManyField(blank=True, to="Place", related_name="tiles")
    primary_categories = ManyToManyField(blank=True, to="PrimaryCategory", related_name="tiles")
    secondary_categories = ManyToManyField(blank=True, to="SecondaryCategory", related_name="tiles")


class Winner(Model):
    name = CharField(max_length=256)
    game = ForeignKey(to="Game", related_name="winners")
    time = DateTimeField()




