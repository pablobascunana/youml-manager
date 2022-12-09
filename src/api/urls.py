from rest_framework.routers import SimpleRouter

from api.viewsets.train.view import TrainViewSet

router = SimpleRouter(trailing_slash=False)

urlpatterns = []

router.register("train", TrainViewSet, basename='train')

urlpatterns += router.urls
