from django.shortcuts import render
from app6_deleteview.models import Dstudent
from django.views.generic.edit import DeleteView
from django.views.generic.base import TemplateView

# Create your views here.
class StudentDeleteView(DeleteView):
    model = Dstudent
    success_url = '/successview/'

class StudentCancel(TemplateView):
    template_name = 'app6_deleteview/cancel_template.html'

class StudentSuccess(TemplateView):
    template_name = 'app6_deleteview/success_template.html'