from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views import generic
from datetime import date
from datetime import datetime
import datetime as dt
import calendar
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


@login_required(login_url='Home')
def lunch_in_out(request):
    if request.user.is_admin or request.user.is_superadmin:
        messages.error(request, 'Access Denied')
        return redirect('Home')
    else:
        employee = Employee.objects.get(account=request.user)
        current_date = date.today()
        timecard = Timecard.objects.get(Q(employee__account=request.user) and Q(day=current_date))

        if not timecard.lunch_in:
            timecard.lunch_in = datetime.now().strftime("%H:%M:%S")
            timecard.save()
            messages.success(request, 'Lunch start, Enjoy your meal')
            return redirect('Home')
        else:
            timecard.lunch_out = datetime.now().strftime("%H:%M:%S")
            timecard.save()
            messages.success(request, 'End of lunch.')
            return redirect('Home')

@login_required(login_url='Home')
def clock_out(request):

    if request.user.is_admin or request.user.is_superadmin:
        messages.error(request, 'Access Denied')
        return redirect('Home')
    else:
        employee = Employee.objects.get(account=request.user)
        current_date = date.today()
        timecard = Timecard.objects.get(Q(employee__account=request.user) and Q(day=current_date))
        timecard.clock_out = datetime.now().strftime("%H:%M:%S")

        t1 = datetime.strptime(f'{timecard.lunch_in}', "%H:%M:%S") - datetime.strptime(f'{timecard.clock_in}', "%H:%M:%S")
        t2 = datetime.strptime(f'{timecard.clock_out}', "%H:%M:%S") - datetime.strptime(f'{timecard.lunch_out}', "%H:%M:%S")
        x = t2 + t1
        timecard.total = (x.seconds) / 3600
        timecard.save()
        messages.success(request, 'Clock out successful, Have a good day')
        return redirect('Home')


@login_required(login_url='Home')
def timesheet(request):

    if request.user.is_admin or request.user.is_superadmin:
        messages.error(request, 'Access Denied')
        return redirect('Home')
    else:
        timecard = Timecard.objects.filter(employee__account=request.user).order_by('day')

        context ={
            'timecard':timecard,
        }

        return render(request, 'timesheet/check_time.html', context)