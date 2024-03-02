from django.shortcuts import render
from django.http import HttpResponse
from app1.forms import StudentForm

# Create your views here.
def home(request):
    studentform = StudentForm
    context = {
        'studentform':studentform
    }
    return render(request,'app1/home.html',context)