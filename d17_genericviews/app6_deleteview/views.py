from django.shortcuts import render
from app6_deleteview.models import Dstudent
from django.views.generic.edit import DeleteView

# Create your views here.
class StudentDeleteView(DeleteView):
    model = Dstudent
    success_url = '/deleted/'