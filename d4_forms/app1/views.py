from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import StudentForm,WidgetForm

# Create your views here.
def home(request):
    initial_val = {'name':"Mahesh",'div':'A'}
    studentform = StudentForm(auto_id='Mahesh_%s',label_suffix="=",initial=initial_val)
    widgetform = WidgetForm
    context = {
        'studentform':studentform,
        'widgetform':widgetform
    }
    return render(request,'app1/home.html',context)