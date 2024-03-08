from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='farmapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('product/<int:product_id>/', views.product_details, name='product_details'),
    path('', views.list_products, name="list_products"),
    path('add_product/', views.add_product, name="add_product"),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('profile/', views.view_profile, name='view_profile'),
    #path('edit_profile/', views.edit_profile, name='edit_profile'),
]