from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..models import Game
from .serializers import GameSerializer


class GameViewSet(ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.all()
    permission_classes = (AllowAny,)
