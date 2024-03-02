from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import StudentForm

# Create your views here.
def home(request):
    initial_val = {'name':"Mahesh",'div':'A'}
    studentform = StudentForm(auto_id='Mahesh_%s',label_suffix="=",initial=initial_val)
    context = {
        'studentform':studentform
    }
    return render(request,'app1/home.html',context)