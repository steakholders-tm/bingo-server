from rest_framework import serializers

from ..models import Game, PrimaryCategory, SecondaryCategory


class SecondaryCategorySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = SecondaryCategory
        fields = ('name', 'description')


class PrimaryCategorySerializer(serializers.ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('name', 'description')


class GameSerializer(serializers.ModelSerializer):
    primary_category = PrimaryCategorySerializer()
    secondary_category = SecondaryCategorySerializer()

    class Meta(object):
        model = Game
        fields = (
            'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category'
        )
