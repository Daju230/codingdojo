# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

from models import *

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, "index.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'])
    return redirect("/users")

def show(request, number):
    context = {
        'user' : User.objects.get(id = number)
    }
    return render(request, "show.html", context)

def destroy(request, number):
    User.objects.get(id = number).delete()
    return redirect("/users")

def edit(request, number):
    context = {
        'user' : User.objects.get(id = number)
    }
    return render(request, "edit.html", context)

def update(request, number):
    x = User.objects.get(id = number)
    x.first_name = request.POST['first_name']
    x.last_name = request.POST['last_name']
    x.email = request.POST['email']
    x.save()
    return redirect('/users/{}'.format(number))

