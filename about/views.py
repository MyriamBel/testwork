# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from Reg.models import People #AbstrUser,
from django.shortcuts import render, get_object_or_404

def about_page(request):
    all_users = People.objects.all()
    output = ', '.join([q.people_first_name for q in all_users]).encode('utf-8')
    context = {'output': output}
    return render(request, 'about/about.html', context)

def about_id_page(request, **id):
    user_id = ''.join(id.values()).encode('ASCII')
    output = get_object_or_404(People, pk=user_id)
    context = {'output': output}
    if user_id:
        return render(request, 'about/about_id.html', context)
