from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# class Profile(TemplateView):
#     template_name = 'registration/profile.html'

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super().dispatch(*args, **kwargs)

@method_decorator(login_required,name='dispatch')
class Profile(TemplateView):
    template_name = 'registration/profile.html'

    