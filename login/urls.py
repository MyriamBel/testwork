# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5
from django.conf.urls import url
from . import views

app_name = 'login'
urlpatterns = [
    url('^$', views.login, name='login_page')
]
