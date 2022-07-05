from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from datetime import datetime
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.contrib import messages, auth
from django.db.models import Q
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

from .models import Timecard
from company.models import Employee
# Create your views here.

@login_required(login_url='Home')
def clock_in(request):
    if request.user.is_admin or request.user.is_superadmin:

        messages.error(request, 'Access Denied')
        return redirect('Home')

    else:
        employee = Employee.objects.get(account=request.user)
        current_date = date.today()
        timecard = Timecard.objects.filter(Q(employee__account=request.user) and Q(day=current_date)).exists()

        if not timecard:
            data = Timecard()
            data.employee = employee
            data.clock_in = datetime.now().strftime("%H:%M:%S")
            data.save()
            messages.success(request, 'Clock In successfull')
            return redirect('Home')
