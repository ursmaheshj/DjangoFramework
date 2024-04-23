from django.shortcuts import render,HttpResponse
from django.core.cache import cache

# Create your views here.
def home(request):
    lc = 0
    if request.user.is_authenticated:
        lc = cache.get('loginCount',version=request.user.pk)
    return HttpResponse(f'Hi {request.user.username or "Anonymous"}, You have logged in {lc} times')
