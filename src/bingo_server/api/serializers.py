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
    primary_category = PrimaryCategorySerializer(read_only=True)
    secondary_category = SecondaryCategorySerializer(read_only=True)
    place = PrimaryCategorySerializer(read_only=True)
    game_type = GameTypeSerializer(read_only=True)

    class Meta(object):
        model = Game
        fields = (
            'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category'
        )


class TileSerializer(ModelSerializer):
    primary_categories = PrimaryCategorySerializer(many=True, read_only=True)

    class Meta(object):
        model = Tile
        fields = ('name', 'primary_categories', 'secondary_categories')


class WinnerSerializer(ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta(object):
        model = Winner
        fields = ('name', 'time', 'game')
