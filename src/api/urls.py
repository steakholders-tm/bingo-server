from rest_framework.routers import DefaultRouter

#
from bingo_server.api import views as bingo_server_views

router = DefaultRouter()

router.register('games', bingo_server_views.GameViewSet)
router.register('primary-categories', bingo_server_views.PrimaryCategoryViewSet)
router.register('secondary-categories', bingo_server_views.SecondaryCategoryViewSet)
router.register('place', bingo_server_views.PlaceViewSet)
router.register('game-type', bingo_server_views.GameTypeViewSet)

urlpatterns = router.urls
