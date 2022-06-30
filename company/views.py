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
from .forms import RegisterEnterprise
from .models import Enterprise
from accounts.models import Account
# Create your views here.

def register_enterprise(request):

    if request.method == 'POST':
        form = RegisterEnterprise(request.POST)
        if form.is_valid():
            enterprise = Enterprise()
            enterprise.name = form.cleaned_data['name']
            enterprise.email = form.cleaned_data['email']
            enterprise.phone = form.cleaned_data['phone']
            enterprise.address_line_1 = form.cleaned_data['address_line_1']
            enterprise.address_line_2 = form.cleaned_data['address_line_2']
            enterprise.state = form.cleaned_data['state']
            enterprise.city = form.cleaned_data['city']
            enterprise.country = form.cleaned_data['country']
            enterprise.zipcode = form.cleaned_data['zipcode']

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

            current_site = get_current_site(request)
            mail_subject = f'Welcome to PayRoll System {enterprise.name}'
            message = render_to_string('enterprise/email_confirmation.html',{
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
