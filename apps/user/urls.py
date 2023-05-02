from rest_framework.routers import DefaultRouter

from apps.user.views import UserApiViewSet

router = DefaultRouter()

router.register(
    prefix="",
    viewset=UserApiViewSet
)

urlpatterns = router.urls
