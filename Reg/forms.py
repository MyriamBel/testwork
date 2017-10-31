from django.forms import ModelForm
from .models import People, User


class RegPeopleForm(ModelForm):
    class Meta:
        model = People
        fields = ['birthday_date', 'about']


class RegUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']

