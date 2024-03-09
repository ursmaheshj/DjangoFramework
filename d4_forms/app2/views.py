from django.shortcuts import render
from app2.forms import RegisterForm

# Create your views here.
def RegisterView(request):
    if request.method == "POST":
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            print(registerform)
            print(registerform.cleaned_data)
    else:
        registerform = RegisterForm()
    return render(request,'app2/form.html',{'registerform':registerform})