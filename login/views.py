# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .forms import LoginUserForm, LoginForm
#from django.shortcuts import redirect
from django.http import HttpResponseRedirect


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if form.get_user():
                login(request, form.get_user())
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})


    # if ('username' in request.GET) and ('password' in request.GET):
    #     username = request.GET['username']
    #     password = request.GET['password']
    #     user = authenticate(username=username, password=password)
    #     if user is not None:
    #         login(user=user)
    #         return HttpResponseRedirect('/')
    #     else:
    #         form = LoginUserForm()
    #         message = 'Пользователь не найден'
    #         return render(request, 'login/login.html', {'form': form, 'message': message})
    # else:
    #     form = LoginUserForm()
    #     return render(request, 'login/login.html', {'form': form})
