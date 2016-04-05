from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.serializers import ModelSerializer
from rest_framework.utils import model_meta

from ..models import Game, GameType, PrimaryCategory, SecondaryCategory, Tile, Winner, Place


class SecondaryCategorySerializer(ModelSerializer):

    class Meta(object):
        model = SecondaryCategory
        fields = ('id', 'name', 'description')


class PrimaryCategorySerializer(ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('id', 'name', 'description')


class GameTypeSerializer(ModelSerializer):

    class Meta(object):
        model = GameType
        fields = ('id', 'name', 'description')


class PlaceSerializer(ModelSerializer):

    class Meta(object):
        model = PrimaryCategory
        fields = ('id', 'name', 'description')


class TileSerializer(ModelSerializer):
    place = PlaceSerializer(many=True, read_only=True)
    primary_categories = PrimaryCategorySerializer(many=True, read_only=True)
    secondary_categories = SecondaryCategorySerializer(many=True, read_only=True)

    class Meta(object):
        model = Tile
        fields = ('id', 'name', 'primary_categories', 'secondary_categories', 'place')


class GameSerializer(ModelSerializer):
    primary_category = PrimaryKeyRelatedField(queryset=PrimaryCategory.objects.all())
    secondary_category = PrimaryKeyRelatedField(required=False, queryset=SecondaryCategory.objects.all())
    place = PrimaryKeyRelatedField(queryset=Place.objects.all())
    game_type = PrimaryKeyRelatedField(queryset=GameType.objects.all())
    tiles = TileSerializer(read_only=True, many=True)

    class Meta(object):
        model = Game
        fields = (
            'id', 'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category', "tiles"
        )

    def create(self, validated_data):

        ModelClass = self.Meta.model

        tiles = self.get_tiles(validated_data)

        try:
            instance = ModelClass.objects.create(**validated_data)
        except TypeError as exc:
            msg = (
                'Got a `TypeError` when calling `%s.objects.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.objects.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception text was: %s.' %
                (
                    ModelClass.__name__,
                    ModelClass.__name__,
                    self.__class__.__name__,
                    exc
                )
            )
            raise TypeError(msg)

        instance.tiles.add(*tiles)
        return instance

    def get_tiles(self, validated_data):
        number_of_tiles = 50
        tiles = []
        tiles.extend(validated_data['place'].tiles.all())
        tiles.extend(validated_data['primary_category'].tiles.all())
        tiles.extend(validated_data['secondary_category'].tiles.all())
        if len(tiles) < number_of_tiles:
            return []

        import random
        random.shuffle(tiles)
        return tiles[:number_of_tiles]


class WinnerSerializer(ModelSerializer):
    game = GameSerializer(read_only=True)

    class Meta(object):
        model = Winner
        fields = ('id', 'name', 'time', 'game')
