from rest_framework.serializers import ModelSerializer

from ..models import Game, PrimaryCategory, SecondaryCategory, GameType


class SecondaryCategorySerializer(ModelSerializer):

    class Meta(object):
        model = SecondaryCategory
        fields = ('name', 'description')


class PrimaryCategorySerializer(ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('name', 'description')


class GameTypeSerializer(ModelSerializer):

    class Meta(object):
        model = GameType
        fields = ('name', 'description')


class PlaceSerializer(ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('name', 'description')


class GameSerializer(ModelSerializer):
    primary_category = PrimaryCategorySerializer()
    secondary_category = SecondaryCategorySerializer()
    place = PrimaryCategorySerializer()
    game_type = GameTypeSerializer()

    class Meta(object):
        model = Game
        fields = (
            'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category'
        )
