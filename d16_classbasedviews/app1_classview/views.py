from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class Demo(View):         
    name = 'Mahesh'
    def get(self,request):
        return HttpResponse(f'<h2>Class Based View | name:{self.name}</h2>')
    