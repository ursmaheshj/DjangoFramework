from django.urls import reverse_lazy
from django import forms
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from genericcbv.models import User

# Create your views here.
class UserListView(ListView):
    model = User

class UserCreateView(CreateView):
    model = User
    fields = ['name','email','age','password']
    success_url = "/"
    def get_form(self):
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
        form.fields['age'].widget = forms.TextInput(attrs={'class':'form-control'})
        form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
        return form
    
class UserDetailView(DetailView):
    model = User
    fields = ['name','email','age','password']

class UserUpdateView(UpdateView):
    model = User
    fields = ['name','email','age','password']
    success_url = "/"
    def get_form(self):
            form = super().get_form()
            form.fields['name'].widget = forms.TextInput(attrs={'class':'form-control'})
            form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control'})
            form.fields['age'].widget = forms.TextInput(attrs={'class':'form-control'})
            form.fields['password'].widget = forms.PasswordInput(attrs={'class':'form-control'})
            return form
    
class UserDeleteView(DeleteView):
    model = User
    success_url = "/"
    
    