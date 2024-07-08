from django.shortcuts import render
from django.views.generic import ListView
from app1_listview.models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    # template_name_suffix = '_get'     #Custom suffix instead of _list use _get
    # template_name = 'app1_listview/student.html'      #Custom template name
    # context_object_name = 'students'    #Custom context name
    ordering = ['-name']