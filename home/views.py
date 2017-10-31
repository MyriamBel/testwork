# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.shortcuts import render

def home_page(request, page, **id):
    if request.user.is_authenticated():
        user = request.user
        return render(request, 'home/home.html', {'user': user})
    else:
        return render(request, 'home/home.html', {})
