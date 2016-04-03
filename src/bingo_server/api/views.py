from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..models import Game, PrimaryCategory, SecondaryCategory
from .serializers import GameSerializer, PrimaryCategorySerializer, SecondaryCategorySerializer


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)


class PrimaryCategoryViewSet(ModelViewSet):
    serializer_class = PrimaryCategorySerializer
    queryset = PrimaryCategory.objects.all()
    permission_classes = (AllowAny,)


class SecodaryCategoryViewSet(ModelViewSet):
    serializer_class = SecondaryCategorySerializer
    queryset = SecondaryCategory.objects.all()
    permission_classes = (AllowAny,)
