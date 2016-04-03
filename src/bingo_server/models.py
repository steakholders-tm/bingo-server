#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db.models import DateField, TimeField, CharField, Model, ManyToManyField, IntegerField, ForeignKey, DateTimeField
CHAR_FIELD = CharField(max_length=256)
CHAR_FIELD_NAME = CharField(max_length=256)
CHAR_FIELD_DESCRIPTION = CharField(blank=True, max_length=512)


# Create your models here.
class Game(Model):
    name = CHAR_FIELD
    date = DateField
    time = TimeField
    duration = IntegerField
    game_type = ForeignKey(to="GameType", related_name="games")
    place = ForeignKey(to="Place", related_name="games")
    primary_category = ForeignKey(to="PrimaryCategory", related_name="games")
    secondary_category = ForeignKey(null=True, blank=True, to="SecondaryCategory", related_name="games")


class GameType(Model):
    name = CHAR_FIELD_NAME
    description = CHAR_FIELD_DESCRIPTION


class Place(Model):
    name = CHAR_FIELD_NAME
    description = CHAR_FIELD_DESCRIPTION


class PrimaryCategory(Model):
    name = CHAR_FIELD_NAME
    description = CHAR_FIELD_DESCRIPTION


class SecondaryCategory(Model):
    name = CHAR_FIELD_NAME
    description = CHAR_FIELD_DESCRIPTION


class Tile(Model):
    text = CHAR_FIELD
    games = ManyToManyField(blank=True, to="Game", related_name="tiles")
    place = ManyToManyField(blank=True, to="Place", related_name="tiles")
    primary_categories = ManyToManyField(blank=True, to="PrimaryCategory", related_name="tiles")
    secondary_categories = ManyToManyField(blank=True, to="SecondaryCategory", related_name="tiles")


class Winner(Model):
    name = CHAR_FIELD_NAME
    game = ForeignKey(to="Game", related_name="winners")
    time = DateTimeField




