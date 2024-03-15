from django.shortcuts import render
from app4.forms import StudentForm,TeacherForm
# Create your views here.

def forminheritance(request):
    studentform = StudentForm()
    teacherform = TeacherForm()

    if request.method == 'POST':
        try:
            if request.POST['student_name']:
                studentform = StudentForm(request.POST)
                if studentform.is_valid():
                    studentform.save()
                teacherform = TeacherForm()
        except:
            teacherform = TeacherForm(request.POST)
            if teacherform.is_valid():
                teacherform.save()
            studentform = StudentForm()

    context = {
        'studentform':studentform,
        'teacherform':teacherform,
    }

    return render(request,'app4/forminheritance.html',context)
        