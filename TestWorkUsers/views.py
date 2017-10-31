# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.contrib.auth import logout
from django.http import HttpResponseRedirect

def logout_f(request):
    logout(request)
    return HttpResponseRedirect('/')