from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class MyTemplateView(TemplateView):
    template_name = 'app2/home.html'

