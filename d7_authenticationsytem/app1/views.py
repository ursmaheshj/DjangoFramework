from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from app1.forms import MyUserCreationForm as UserCreationForm
from django.contrib import messages

# Create your views here.
def sign_up(request):
    fm = UserCreationForm()
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'User has been created!')
    return render(request,'app1/registration.html',{'form':fm})
