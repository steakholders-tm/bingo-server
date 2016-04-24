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
    secondary_category = PrimaryKeyRelatedField(required=False,
                                                allow_null=True,
                                                queryset=SecondaryCategory.objects.all())
    place = PrimaryKeyRelatedField(queryset=Place.objects.all())
    game_type = PrimaryKeyRelatedField(queryset=GameType.objects.all())
    tiles = TileSerializer(read_only=True, many=True)

    class Meta(object):
        model = Game
        fields = (
            'id', 'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category',
            "tiles", 'active'
        )

    def create(self, validated_data):
        instance = super().create(validated_data)

        tiles = self.get_tiles(validated_data)

        instance.tiles.add(*tiles)
        return instance

    def get_tiles(self, validated_data, number_of_tiles=25):
        tiles = []
        place = validated_data['place']
        if place:
            tiles.extend(place.tiles.all())
        pc = validated_data['primary_category']
        if pc:
            tiles.extend(pc.tiles.all())
        sc = validated_data['secondary_category']
        if sc:
            tiles.extend(sc.tiles.all())
        if len(tiles) < number_of_tiles:
            return []

        import random
        tiles = random.shuffle(tiles)
        return tiles[:number_of_tiles]


class WinnerSerializer(ModelSerializer):

    class Meta(object):
        model = Winner
        fields = ('id', 'name', 'time', 'game')
