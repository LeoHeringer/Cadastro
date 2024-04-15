from django.contrib import admin
from django.urls import path, include

from .import views

urlpatterns = [
    path('get-all-users-xml', views.get_users_xml),
    path('get-all-users-json', views.get_users_json),
    path('user-xml', views.get_by_nick_xml),
    path('user-json', views.get_by_nick_json),
    path('create-user-xml', views.create_user_xml),
    path('create-user-json', views.create_user_json),
    path('update-user-xml', views.update_user_xml),
    path('update-user-json', views.update_user_json),
    path('delete-user-xml', views.delete_user_xml),
    path('delete-user-json', views.delete_user_json),
]
