from rest_framework.routers import DefaultRouter

#
from bingo_server.api import views as bingo_server_views

router = DefaultRouter()

router.register('games', bingo_server_views.GameViewSet)
router.register('game-type', bingo_server_views.GameTypeViewSet)
router.register('place', bingo_server_views.PlaceViewSet)
router.register('primary-categories', bingo_server_views.PrimaryCategoryViewSet)
router.register('secondary-categories', bingo_server_views.SecondaryCategoryViewSet)
router.register('tiles', bingo_server_views.TileViewSet)
router.register('winners', bingo_server_views.WinnerViewSet)

urlpatterns = router.urls
