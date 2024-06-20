from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.

class MyRedirectView(RedirectView):
    pattern_name='mindex'