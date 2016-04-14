from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import Game, GameType, Place, PrimaryCategory, SecondaryCategory, Tile, Winner
from .serializers import GameSerializer, GameTypeSerializer, PlaceSerializer, PrimaryCategorySerializer, \
    SecondaryCategorySerializer, TileSerializer, WinnerSerializer


class GameViewSet(GenericViewSet, CreateModelMixin, ListModelMixin, RetrieveModelMixin):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)


class PrimaryCategoryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PrimaryCategorySerializer
    queryset = PrimaryCategory.objects.all()
    permission_classes = (AllowAny,)


class SecondaryCategoryViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = SecondaryCategorySerializer
    queryset = SecondaryCategory.objects.all()
    permission_classes = (AllowAny,)


class PlaceViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = (AllowAny,)


class GameTypeViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = GameTypeSerializer
    queryset = GameType.objects.all()
    permission_classes = (AllowAny,)


class TileViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = TileSerializer
    queryset = Tile.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = ('games', 'primary_categories', 'secondary_categories')


class WinnerViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = WinnerSerializer
    queryset = Winner.objects.all()
    permission_classes = (AllowAny,)
    filter_fields = ('game',)
