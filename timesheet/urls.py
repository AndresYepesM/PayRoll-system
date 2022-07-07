from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from .views import *

urlpatterns = [

    path('clock/in', clock_in, name='clock_in'),

    path('lunch/in/out', lunch_in_out, name='lunch_in_out'),

    path('clock/out', clock_out, name='clock_out'),

    path('my/timesheet/', timesheet, name='timesheet'),
]