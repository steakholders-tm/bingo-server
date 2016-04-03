from rest_framework.serializers import ModelSerializer

from ..models import Game, PrimaryCategory, SecondaryCategory


class SecondaryCategorySerializer(ModelSerializer):

    class Meta(object):
        model = SecondaryCategory
        fields = ('name', 'description')


class PrimaryCategorySerializer(ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('name', 'description')


class PlaceSerializer(ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('name', 'description')


class GameSerializer(ModelSerializer):
    primary_category = PrimaryCategorySerializer()
    secondary_category = SecondaryCategorySerializer()
    place = PrimaryCategorySerializer()

    class Meta(object):
        model = Game
        fields = (
            'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category'
        )
