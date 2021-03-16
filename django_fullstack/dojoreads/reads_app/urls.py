from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('add', views.add_book),
    path('create', views.create_book),
    path('<int:book_id>', views.single_book),
    path('<int:book_id>/add_review', views.create_review),
    path('reviews/<int:review_id>/delete', views.delete_review)

]