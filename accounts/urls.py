from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from accounts.views import *

urlpatterns = [
    path('login/', login, name='login'),

    path('logout/', logout, name='logout'),

    path('new_employee/', new_employee, name='new_employee'),

    path('designate_role/<int:user_id>/', designate_role, name='designate_role'),
]