from django.shortcuts import render
from django.contrib import messages
from app.models import Student
from app.forms import StudentForm

# Create your views here.
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