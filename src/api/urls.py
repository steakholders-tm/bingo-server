from rest_framework.routers import SimpleRouter

#
from bingo_server.api import views as bingo_server_views

router = SimpleRouter()

router.register('games', bingo_server_views.GameViewSet)
router.register('primary-categories', bingo_server_views.PrimaryCategoryViewSet)

urlpatterns = router.urls
