# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from ..login_app.models import User
from models import Poke


# Create your views here.
def dashboard(request):
    context = {
        'otherUsers': User.objects.exclude(id = request.session['id']),
        'curUser':  User.objects.get(id = request.session['id']),
    }
    return render(request, 'poke_app/dashboard.html', context)

def addpoke(request, id):
    Poke.objects.create(giver = User.objects.get(id = request.session['id']), receiver = User.objects.get(id = id)),
    return redirect('/poke')