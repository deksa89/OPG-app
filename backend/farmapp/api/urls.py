from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, ProductViewSet

# Create a router and register our viewsets with it.
post_router = DefaultRouter()
post_router.register(r'farms', FarmViewSet)
post_router.register(r'products', ProductViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(post_router.urls)),
]
