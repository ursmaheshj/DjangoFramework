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
            messages.info(request,'Now he can login!!!')
    else:
        studentform = StudentForm()

    return render(request,'app/registration.html',{'studentform':studentform})