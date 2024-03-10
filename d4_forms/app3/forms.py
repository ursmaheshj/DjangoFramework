from django.core import validators
from django import forms

def check_email_domain(value):
    if value[-10:]!='@gmail.com':
        raise forms.ValidationError('Incorrect Domain')

class StudentForm(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(4)])
    email = forms.EmailField(validators=[check_email_domain])
    