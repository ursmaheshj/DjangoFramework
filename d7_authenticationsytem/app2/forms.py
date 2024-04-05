from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class MyUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_joined'].disabled = True
        self.fields['last_login'].disabled = True

class MyAdminUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = '__all__'
        labels = {'email':'Email'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_joined'].disabled = True
        self.fields['last_login'].disabled = True