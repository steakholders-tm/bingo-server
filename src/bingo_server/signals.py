from django.db.models.signals import post_save
from django.dispatch import receiver

from bingo_server.models import Winner


@receiver(post_save, sender=Winner)
def deactivate_game_when_won(sender, instance, created, **kwargs):
    instance.game.active = False
    instance.game.save()
