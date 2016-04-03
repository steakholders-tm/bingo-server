from rest_framework import serializers

from ..models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta(object):
        model = Game
        fields = (
            'name', 'date', 'time', 'duration', 'game_type', 'place', 'primary_category', 'secondary_category'
        )
