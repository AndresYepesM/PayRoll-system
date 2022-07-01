from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('register_enterprise/', register_enterprise, name='register_enterprise'),

    path('register_new_employee/', register_new_employee, name='register_new_employee'),

    path('activation/<uidb64>/<token>/', activate, name='activate'),
]