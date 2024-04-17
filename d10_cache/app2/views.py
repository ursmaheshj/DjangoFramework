from django.shortcuts import render
from time import sleep
from django.views.decorators.cache import cache_page

# Create your views here.
# @cache_page(20)
# def perviewhome(request):
#     print("start processing")
#     sleep(5)
#     print('processing completed')
#     return render(request,'app2/home.html')

def perviewhome(request):
    print("start processing")
    sleep(5)
    print('processing completed')
    return render(request,'app2/home.html')