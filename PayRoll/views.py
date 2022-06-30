from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages, auth
from datetime import date
from random import *
from company.models import Enterprise

def home(request):
    if request.user.is_authenticated:
        x = Enterprise.objects.get(account=request.user.id)
        print(x.name, x.phone, x.id)

    return render(request, 'mains/home.html')