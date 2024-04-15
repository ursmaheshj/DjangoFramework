from django.shortcuts import render
from time import sleep

# Create your views here.
def home(request):
    print("start processing")
    sleep(5)
    print('processing completed')
    return render(request,'app1/home.html')