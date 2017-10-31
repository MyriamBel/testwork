# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegPeopleForm, RegUserForm


def createuser(request):
    if request.method == "POST":
        uform = RegUserForm(data=request.POST)
        pform = RegPeopleForm(data=request.POST)
        if uform.is_valid() and pform.is_valid():
            user = uform.save()
            people = pform.save(commit=False)
            people = user
            people.save()
        return HttpResponseRedirect('/')
    else:
        uform=RegUserForm()
        pform=RegPeopleForm()
        return render(request, 'registration/registration.html', {'uform': uform, 'pform': pform})




