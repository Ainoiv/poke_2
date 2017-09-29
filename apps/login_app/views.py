# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import User
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'login_app/index.html')

def create(request):
    results = User.objects.validate(request.POST)
    if results['status'] == True:
        user = User.objects.creator(request.POST)
        messages.success(request, 'User has been created SUCCESSFULLY!')

    else:
        for error in results['errors']:
            messages.error(request, error)
    
    return redirect('/')

def login(request):
    results = User.objects.loginVal(request.POST)
    if results['status'] == False:
        messages.error(request, 'PLEASE check you EMAIL or PASSWORD and try AGAIN!')
        return redirect('/')
    request.session['email'] = results['user'].email
    request.session['first_name'] = results['user'].first_name
    request.session['id'] = results['user'].id
    return redirect('/poke/')

def logout(request):
    request.session.flush()
    return redirect('/')