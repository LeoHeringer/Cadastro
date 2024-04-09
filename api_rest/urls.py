from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/<str:nick>', views.get_by_nick),
    path('create-user/', views.create_user),
    path('update-user', views.update_user),
    path('delete-user', views.delete_user)
]
