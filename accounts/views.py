from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages, auth
from django.db.models import Q
from .models import Account


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)

        if not user:
            messages.error(request, 'Email or Password incorrect, please try again')
            return redirect('Home')
        else:
            auth.login(request, user)
            messages.success(request, 'Welcome back')
            return redirect('Home')

    return render(request, 'mains/home.html')

@login_required(login_url='Home')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfull, have a nice day')
    return redirect('Home')