from django.shortcuts import render
from app1.models import User
from app1.forms import UserForm

# Create your views here.
def UserView(request):
    userform = UserForm()

    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data['name']
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            user = User(name=name,email=email,password=password)
            user.save()
        
    users = User.objects.all()
    context = {
        'users' :users,
        'userform' : userform,
    }
    return render(request,'app1/home.html',context)