from django.conf.urls import include
from django.urls import path
from rest_framework import routers

from posts import views

router = routers.SimpleRouter()
router.register("posts", views.PostViewSet, basename="posts")

urlpatterns = [path("api/v1/", include(router.urls))]
