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
from random import *
from company.models import Enterprise, Employee
from timesheet.models import Timecard

def home(request):
    current_date = date.today()
    check = Timecard.objects.filter(Q(employee__account=request.user) and Q(day=current_date)).exists()
    
    if check:
        timecard = Timecard.objects.get(Q(employee__account=request.user) and Q(day=current_date))
    else:
        timecard = None
    
    context = {
        'check':check,
        'timecard':timecard,
    }
    return render(request, 'mains/home.html', context)