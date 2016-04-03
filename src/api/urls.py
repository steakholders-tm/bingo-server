from rest_framework.routers import DefaultRouter

#
from bingo_server.api import views as bingo_server_views

router = DefaultRouter()

router.register('games', bingo_server_views.GameViewSet)

urlpatterns = router.urls
