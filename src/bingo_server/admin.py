from django.contrib import admin
from .models import Game, Place, Winner, Tile, PrimaryCategory, SecondaryCategory, GameType

# Register your models here.

admin.site.register(Game)
admin.site.register(Place)
admin.site.register(Winner)
admin.site.register(Tile)
admin.site.register(PrimaryCategory)
admin.site.register(SecondaryCategory)
admin.site.register(GameType)