from django import forms
from app1_listview.models import Student

# using app1_listview model
class StudentForm(forms.ModelForm):
    class Meta:
        model =  Student
        fields = '__all__'
