from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib import messages, auth
from django.db.models import Q
from .models import Account, Department
from .forms import UserRegistration, DesignateRole


# Login Function
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

# Logout function
@login_required(login_url='Home')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout successfull, have a nice day')
    return redirect('Home')            

# Registration Form
@login_required(login_url='Home')
def new_employee(request):
    if request.user.is_admin:
        if request.method == 'POST':
            form = UserRegistration(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name= form.cleaned_data['first_name']
                email = form.cleaned_data['email']
                phone = form.cleaned_data['phone']
                username = email.split("@")[0]
                password = form.cleaned_data['password']
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.phone = phone
                user.is_active = True
                user.save()
                messages.success(request, 'Step 2: Designate role of the new employee')
                return redirect('designate_role', user_id=user.id)
        else:
            form = UserRegistration()

        context ={ 
            'form':form,
        }
        
        return render(request, 'accounts/new_employee.html', context)
    else:
        messages.error(request, 'Access Denied')
        return redirect('Home')
    
   

@login_required(login_url='Home')
def designate_role(request, user_id):
    if request.user.is_admin:
        user = get_object_or_404(Account, id=user_id)
        if request.method == 'POST':
            form = DesignateRole(request.POST, instance=user)
            if form.is_valid():
                data = Department()
                data.account = user
                data.ssn = form.cleaned_data['ssn']
                data.address = form.cleaned_data['address']
                data.salary = form.cleaned_data['salary']
                data.role = form.cleaned_data['role']
                data.sector = form.cleaned_data['sector']
                data.save()
                messages.success(request, 'New employee registed successfull')
                return redirect('Home')
        else:
            form = DesignateRole(instance=user)

        context = {
            'form':form,
        }
        return render(request, 'accounts/designate_role.html', context)
    else:
        messages.error(request, 'Access Denied')
        return redirect('Home')

