from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(required=False,help_text="Demo help")
    div = forms.CharField()
    code = forms.IntegerField()
    about = forms.CharField(widget=forms.Textarea)
    key = forms.CharField(widget=forms.HiddenInput())
