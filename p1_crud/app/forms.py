from django import forms
from app.models import User

class UserForm(forms.ModelForm):
    show_password = forms.CharField(widget=forms.CheckboxInput(attrs={'onclick':'myFunction()'}),required=False)
    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control','id':'myInput'})
        }