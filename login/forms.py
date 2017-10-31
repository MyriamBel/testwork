# -*- coding: utf-8 -*-
#!/usr/bin/env python3.5

from django.forms import ModelForm, Form
from Reg.models import User
from django import forms
from django.contrib.auth import authenticate

class LoginUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class LoginForm(Form):
    username = forms.CharField(label=u'Имя пользователя')
    password = forms.CharField(label=u'Пароль', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if not self.errors:
            user = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if user is None:
                raise forms.ValidationError(u'Имя пользователя и пароль не подходят')
            self.user = user
        return cleaned_data

    def get_user(self):
        return self.user or None