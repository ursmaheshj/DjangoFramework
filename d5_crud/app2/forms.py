from app1.models import User
from django import forms

class ModelUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {'name':'Enter Name','email':'Enter Email','password':'Enter Pass...'}
        error_messages = {'name':{'required':'Naam likhna jaruri che'},
                          'email':{'required':'Email bhi jaruri hai bava'}}
        widgets = {'password':forms.PasswordInput,
                   'name':forms.TextInput(attrs={'class':'myclass','placeholder':'Apna naam likhiye'})}
        