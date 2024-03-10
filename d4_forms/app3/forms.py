from django.core import validators
from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(validators=[validators.MaxLengthValidator(4)])
    email = forms.EmailField()
    