from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('user/register', views.register),
    path('user/login', views.login),
    path('user/logout', views.logout),
    path('quotes', views.quotes),
    path('create', views.create),
    path('like/<int:quote_id>', views.add_like),
    path('delete/<int:quote_id>', views.delete),
    path('user/<int:user_id>', views.show_user),
    path('myaccount/<int:user_id>', views.edit_user),
    path('myaccount/update/<int:user_id>', views.update)
]