from django.core import validators
from django import forms

def check_email_domain(value):
    if value[-10:]!='@gmail.com':
        raise forms.ValidationError('Incorrect Domain')

class StudentForm(forms.Form):
    error_css_class = 'E_error'
    required_css_class = 'E_required'
    name = forms.CharField(validators=[validators.MaxLengthValidator(4)])
    email = forms.EmailField(validators=[check_email_domain])   
    password1 = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)
    def clean(self):
        cleaned_data = super().clean()
        paas1 = self.cleaned_data['password1']
        paas2 = self.cleaned_data['password2']
        if paas1 != paas2:
            raise forms.ValidationError('Password doesnt match')