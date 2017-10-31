# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.shortcuts import render

def home_page(request, page, **id):
    if request.user.is_authenticated():
        return render(request, 'home/home_auth.html', {})
    else:
        return render(request, 'home/home_non_auth.html', {})
