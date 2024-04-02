from rest_framework.routers import DefaultRouter
from farmapp.api.urls import post_router
from django.urls import path, include


router = DefaultRouter()

router.registry.extend(post_router.registry)

urlpatterns = [
    path('', include(router.urls))
]