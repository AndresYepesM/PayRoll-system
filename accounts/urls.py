from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from accounts import views

urlpatterns = [
    path('login/', views.login, name='login'),

    path('logout/', views.logout, name='logout'),
]