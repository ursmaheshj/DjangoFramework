from django import forms
from app4.models import User


class StudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_name','email','password']
        widgets = {'password':forms.PasswordInput}

class TeacherForm(StudentForm):
    class Meta(StudentForm.Meta):
        fields = ['teacher_name','email','password']