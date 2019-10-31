"""
gateway/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_page, name='login_page'),
    path('register', views.register_page, name='register_page'),
    path('register/ok', views.register_success, name='registered_page'),
    path('api/login', views.post_login_api, name='login_api'),
    path('api/register', views.post_register_api, name='register_api'),
]
