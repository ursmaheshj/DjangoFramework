from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView
from app5_updateview.models import Ustudent

# Create your views here.
class StudentUpdateCreateView(CreateView):
    model = Ustudent
    fields = ['name','roll','course']
    success_url = '/updatecreateview/'

class StudentUpdateView(UpdateView):
    model = Ustudent
    fields = ['name','roll','course']
    # success_url = '/thankyou/'

    def get_success_url(self) -> str:
        pk = self.kwargs['pk']
        return f'/updateview/{pk}'