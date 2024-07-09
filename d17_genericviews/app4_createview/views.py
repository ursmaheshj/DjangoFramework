from django.forms import BaseModelForm
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from app4_createview.models import Cstudent 
from django import forms

# Create your views here.
class StudentCreateView(CreateView):
    model = Cstudent
    fields = ['name','roll','course']
    # success_url = '/createview/'
    
    #1to add class to form fields
    # form_class = 'FormClass created in forms.py'   #We can add our attrs and class in forms.py
    #2to add class to form fields
    def get_form(self, form_class: type[BaseModelForm] | None = ...) -> BaseModelForm:
        form = super().get_form()
        form.fields['name'].widget = forms.TextInput(attrs={'class':'myClass'})
        form.fields['roll'].widget = forms.TextInput(attrs={'class':'myrollClass'})
        form.fields['course'].widget = forms.TextInput(attrs={'class':'myClass'})
        return form
    
class StudentCreateDetailView(DetailView):
    model = Cstudent