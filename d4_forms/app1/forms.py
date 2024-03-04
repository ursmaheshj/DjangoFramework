from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(required=False,help_text="Demo help")
    div = forms.CharField(label='Your division',initial='A+',disabled=True)
    code = forms.IntegerField(error_messages={"required": "Please enter your name"})
    about = forms.CharField(widget=forms.Textarea)
    key = forms.CharField(widget=forms.HiddenInput())

class WidgetForm(forms.Form):
    no_widget = forms.CharField()
    attr_with_widget = forms.CharField(widget=forms.TextInput(attrs={'class':'class1 some1','id':'uniqueid'}))
    passwidget = forms.CharField(widget=forms.PasswordInput)
    textareawidget = forms.CharField(widget=forms.Textarea)
    checkboxwidget = forms.CharField(widget=forms.CheckboxInput)
    filewidget = forms.CharField(widget=forms.FileInput)