from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.

class MyRedirectView(RedirectView):
    pattern_name='mindex'
    permanent = True #change status code from 301 to 302 indicating permanent redirect