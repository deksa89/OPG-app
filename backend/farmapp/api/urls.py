from django.urls import path
from .views import RegisterApi, LoginApi, UserApi, LogoutApi, CreateProduct

urlpatterns = [
    path('register/', RegisterApi.as_view(), name='register'),
    path('login/', LoginApi.as_view(), name='login'),
    path('auth/', UserApi.as_view(), name='auth'),
    path('logout/', LogoutApi.as_view(), name='logout'),
    path('create_product/', CreateProduct.as_view(), name='create_product'),
]