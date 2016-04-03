from rest_framework.serializers import ModelSerializer

from ..models import Game, GameType, PrimaryCategory, SecondaryCategory, Tile, Winner


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


class TileSerializer(ModelSerializer):
    class Meta(object):
        model = Tile
        fields = ('name', 'games', 'place', 'primary_categories', 'secondary_categories')


class WinnerSerializer(ModelSerializer):
    class Meta(object):
        model = Winner
        fields = ('name', 'game', 'time')
