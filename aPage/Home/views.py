# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required()
def index(request):
    return HttpResponse('Hello World')

@login_required()
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request,r'/')
    else:
        # Return an 'invalid login' error message.
        return render(request,r'/')

def logout_view(request):
    logout(request)
    # Redirect to a success page.