from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    email = forms.EmailField()
    subject = forms.CharField()
