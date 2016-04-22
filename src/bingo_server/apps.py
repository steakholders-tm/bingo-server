from django.apps import AppConfig


class BingoServerConfig(AppConfig):
    name = 'bingo_server'

    def ready(self):
        super().ready()

        from bingo_server import signals
