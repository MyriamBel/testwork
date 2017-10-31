# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


class People(models.Model):
    user_number = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday_date = models.DateField()
    about = models.CharField(max_length=255)

    def __unicode__(self):
        return self.user_number




