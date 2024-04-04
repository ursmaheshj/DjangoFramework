from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from django import forms

class MyUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','date_joined','last_login']
        labels = {'email':'Email'}
        # widgets = {'date_joined':forms.DateField(disabled=True)}
        # # attrs = {'date_joined':disabled}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_joined'].disabled = True
        self.fields['last_login'].disabled = True