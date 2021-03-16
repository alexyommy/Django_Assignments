from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users/register', views.register_user),
    path('users/login', views.login_user),
    path('users/<int:user_id>', views.single_user),
    path('logout', views.logout)
]