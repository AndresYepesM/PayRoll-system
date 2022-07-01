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
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from .forms import RegisterEnterprise, EmployeeRegistration
from .models import Enterprise, Employee, Position
from accounts.models import Account
# Create your views here.

def register_enterprise(request):
    if request.method == 'POST':
        form = RegisterEnterprise(request.POST)
        if form.is_valid():
            enterprise = Enterprise()

            # Enterprise information
            enterprise.name = form.cleaned_data['name']
            enterprise.email = form.cleaned_data['email']
            enterprise.phone = form.cleaned_data['phone']
            enterprise.address_line_1 = form.cleaned_data['address_line_1']
            enterprise.address_line_2 = form.cleaned_data['address_line_2']
            enterprise.state = form.cleaned_data['state']
            enterprise.city = form.cleaned_data['city']
            enterprise.country = form.cleaned_data['country']
            enterprise.zipcode = form.cleaned_data['zipcode']

            # Enterprise Account Information
            username = enterprise.email.split('@')[0]
            first_name = enterprise.name.split(' ')[0]
            last_name = enterprise.name.split(' ')[1]
            password = hash(enterprise.email)
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=enterprise.email, password=str(password))
            user.phone = enterprise.phone
            user.is_active = True
            user.is_admin = True
            user.save()
            enterprise.account = user
            enterprise.save()

            mail_subject = f'Welcome to PayRoll System {enterprise.name}'
            message = render_to_string('accounts/email_confirmation.html',{
                'user':user,
                'password':password,
                'enterprise':enterprise,
            })
            to_email=enterprise.email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()

            messages.success(request, 'Your account credential are send to the company email welcome to PayRoll System')
            return redirect('Home')
    else:
        form = RegisterEnterprise()
    
    context ={
        'form':form,
    }

    return render(request, 'enterprise/register_enterprise.html', context)


@login_required(login_url='Home')
def register_new_employee(request):
    if request.user.is_admin or request.user.is_superadmin:
        enterprise = Enterprise.objects.get(account=request.user)
        if request.method == 'POST':
            form = EmployeeRegistration(request.POST, request=request)
            if form.is_valid():
                employee = Employee()

                # Employee Information
                employee.full_name = form.cleaned_data['full_name']
                employee.email = form.cleaned_data['email']
                employee.phone = form.cleaned_data['phone']
                employee.ssn = form.cleaned_data['ssn']
                employee.salary = form.cleaned_data['salary']
                employee.role = form.cleaned_data['role']

                # Employee Account information
                username = employee.email.split('@')[0]
                first_name = employee.full_name.split(' ')[0]
                last_name =  employee.full_name.split(' ')[1]
                password = hash(employee.email)
                user = Account.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=employee.email, password=str(password))
                user.phone = employee.phone
                user.save()
                employee.account = user
                employee.enterprise = enterprise
                employee.save()
                

                current_site = get_current_site(request)
                mail_subject = 'This is a activation Email'
                message = render_to_string('accounts/verification_email.html',{
                    'user':user,
                    'enterprise':enterprise,
                    'domain':current_site,
                    'password':password,
                    'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                    'token':default_token_generator.make_token(user),

                })

                to_email = employee.email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()

                messages.success(request, 'Your new employee is create and the verification email was send')
                return redirect('Home')
        else:
            form = EmployeeRegistration(request=request)

        context = {
            'form':form,
        }

        return render(request, 'enterprise/register_new_employee.html', context)
    else:
        message.error(request, 'Access Denied')
        return redirect('Home')



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations your account is activate!')
        return redirect('Home')
    else:
        messages.error(request, 'Token is already been used')
        return redirect('Home')