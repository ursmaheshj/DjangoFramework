from django.shortcuts import render

# Create your views here.
def addshowview(request):
    return render(request,'app/addandshow.html')
