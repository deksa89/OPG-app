from django.urls import path
from .views import RegisterAPI, LoginAPI, UserApi, LogoutAPI

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('auth/', UserApi.as_view(), name='auth'),
    path('logout/', LogoutAPI.as_view(), name='logout')
]