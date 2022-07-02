from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [
    path('register/enterprise/', register_enterprise, name='register_enterprise'),

    path('register/new/employee/', register_new_employee, name='register_new_employee'),

    path('activation/<uidb64>/<token>/', activate, name='activate'),

    path('employee/list/', employee_list, name='employee_list'),

    path('emplyee/edit/<int:employee_id>/', employee_edit, name='employee_edit'),

    path('employee/access/<int:employee_id>/', employee_access, name='employee_access'),

    path('employee/delete/<int:employee_id>/', employee_delete, name='employee_delete'),

    path('positions/', positions_list, name='positions_list'),

    path('positions/create', positions_create, name='positions_create'),
]