from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        fm = AuthenticationForm(request,request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upass = fm.cleaned_data['password']
            user = authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                messages.success(request,'User has been logged in!!!')
                return HttpResponseRedirect('/profile/')
    else:
        fm = AuthenticationForm()
    return render(request,'app2/login.html',{'form':fm})
    
def profile(request):
    return render(request,'app2/profile.html')