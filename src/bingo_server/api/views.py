from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..models import Game, PrimaryCategory, SecondaryCategory, Place
from .serializers import GameSerializer, PrimaryCategorySerializer, SecondaryCategorySerializer, PlaceSerializer


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)


class PrimaryCategoryViewSet(ModelViewSet):
    serializer_class = PrimaryCategorySerializer
    queryset = PrimaryCategory.objects.all()
    permission_classes = (AllowAny,)


class SecondaryCategoryViewSet(ModelViewSet):
    serializer_class = SecondaryCategorySerializer
    queryset = SecondaryCategory.objects.all()
    permission_classes = (AllowAny,)


class PlaceViewSet(ModelViewSet):
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
    permission_classes = (AllowAny,)