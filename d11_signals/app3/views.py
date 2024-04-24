from django.shortcuts import render,HttpResponse
from app3.signals import notification

# Create your views here.
def custom_signal(request):
    print('Custom Signal')
    notification.send(sender=None,request=request,user='Mahesh')
    return HttpResponse('Custom Signal Demo')