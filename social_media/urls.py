from django.urls import path, include
from rest_framework import routers

from social_media.views import ProfileViewSet, PostViewSet

app_name = "social_media"
router = routers.DefaultRouter()
router.register("profiles", ProfileViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
