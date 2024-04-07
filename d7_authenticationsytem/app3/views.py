from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
def Dashboard(request):
    if request.user.is_authenticated:
        pass    
    else:
        return HttpResponseRedirect('/login/')