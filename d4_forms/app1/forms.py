from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(required=False)
    div = forms.CharField()
    code = forms.IntegerField()
    about = forms.CharField(widget=forms.Textarea)
