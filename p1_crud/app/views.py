from django.shortcuts import render,HttpResponseRedirect

from app.models import User
from app.forms import UserForm

# Create your views here.
def addshowview(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            userform.save()

    users = User.objects.all()
    context = {
        'userform':userform,
        'users':users
    }
    return render(request,'app/addandshow.html',context)

def deleteuser(request,id):
    if request.method == 'POST':
        user = User.objects.get(id=id)
        user.delete()

    return HttpResponseRedirect('/')

def edituser(request,id):
    user = User.objects.get(id=id)
    userform = UserForm(instance=user)
    if request.method == 'POST':
        userform = UserForm(request.POST,instance=user)
        if userform.is_valid():
            userform.save()
    
    return render(request,'app/update.html',{'userform':userform})
