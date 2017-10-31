# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5
from django.conf.urls import url
from . import views

app_name = 'about'
urlpatterns = [
    url(r'^$', views.about_page, name='about_page'),
    url(r'^(?P<id>[0-9]+)/', views.about_id_page, name='profile'),
]
