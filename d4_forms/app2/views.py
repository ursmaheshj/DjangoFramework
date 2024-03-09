from django.shortcuts import render
from app2.forms import RegisterForm,FieldDemoForm

# Create your views here.
def RegisterView(request):
    if request.method == "POST":
        registerform = RegisterForm(request.POST)
        if registerform.is_valid():
            print(registerform)
            print(registerform.cleaned_data)
    else:
        registerform = RegisterForm()
    fielddemoform = FieldDemoForm()
    return render(request,'app2/form.html',{'registerform':registerform,'fielddemoform':fielddemoform})