from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..models import Game, PrimaryCategory
from .serializers import GameSerializer, PrimaryCategorySerializer


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)


class PrimaryCategoryViewSet(ModelViewSet):
    serializer_class = PrimaryCategorySerializer
    queryset = PrimaryCategory.objects.all()
    permission_classes = (AllowAny,)
