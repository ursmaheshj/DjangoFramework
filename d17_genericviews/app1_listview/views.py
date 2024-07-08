from django.shortcuts import render
from django.views.generic import ListView
from app1_listview.models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    # template_name = 'student.html'      #Custom template name
    # context_object_name = 'students'    #Custom context name