from django.shortcuts import render
from django.contrib import messages
from app.models import Student
from app.forms import StudentForm

# Create your views here.
def getmessages(request):

    messages.debug(request,'This is debug') #This wont be visible as default level is 20
    messages.info(request,'This is info')
    messages.success(request,'This is success')
    messages.warning(request,'This is warning')
    messages.error(request,'This is error')

    return render(request,'app/messages.html')

def registration(request):
    if request.method == 'POST':
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            studentform.save()
            messages.add_message(request,messages.SUCCESS,'Profile has been added.')
            print(messages.get_level(request))
            messages.debug(request,'This is debug message')
            messages.info(request,'Now he can login!!!')
            messages.set_level(request,10)
            messages.debug(request,'This is new debug message')
    else:
        studentform = StudentForm()

    return render(request,'app/registration.html',{'studentform':studentform})