from django.shortcuts import render
from app3.forms import StudentForm
# Create your views here.
def StudentView(request):
    if request.method == "POST":
        studentform = StudentForm(request.POST)
        if studentform.is_valid():
            print(studentform)
            print(studentform.cleaned_data)
    else:
        studentform = StudentForm()
    
    return render(request,'app3/student.html',{'studentform':studentform})