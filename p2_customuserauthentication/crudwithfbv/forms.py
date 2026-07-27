from django import forms
from crudwithfbv.models import User

class UserModelForm(forms.ModelForm):
    roles = {'cusotmer':'customer','seller':'seller'}
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    role = forms.ChoiceField(choices=roles)
    class Meta:
        model = User
        fields = ['email','city','role','password','confirm_password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password!=confirm_password:
            self.add_error('confirm_password',"Passwords do not match")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("User with email already exists")
        return email