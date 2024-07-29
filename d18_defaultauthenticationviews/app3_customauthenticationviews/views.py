from django.shortcuts import render
from django.contrib.auth.views import LoginView
from app3_customauthenticationviews.forms import LoginForm


# Create your views here.
class MyLoginView(LoginView):
    template_name='myapp/login.html'
    form_class=LoginForm