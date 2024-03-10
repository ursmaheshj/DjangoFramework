from django import forms

class RegisterForm(forms.Form):
    name = forms.CharField()
    roll = forms.IntegerField()
    email = forms.EmailField()
    subject = forms.CharField()
    # def clean_name(self):
    #     data = self.cleaned_data["name"]
    #     if len(data)<4:
    #         raise forms.ValidationError('Length is less than 4')
    #     return data
    def clean(self):
        cleaned_data = super().clean()
        valname = cleaned_data['name']
        if valname[0]!="M":
            raise forms.ValidationError('Name should start with M')
        valemail = cleaned_data['email']
        if valemail[-10:]!='@gmail.com':
            raise forms.ValidationError('Email should be gmail.com')

class FieldDemoForm(forms.Form):
    charfield = forms.CharField(min_length=5,max_length=10,
                                strip=False,empty_value='Default',
                                error_messages={'required':'Enter data'})
    booleanfield = forms.BooleanField(label='Agree')
    integerfield = forms.IntegerField(min_value=1,max_value=10)
    decimalfield = forms.DecimalField(min_value=5,max_value=20,max_digits=1,decimal_places=2)
    floatfield = forms.FloatField(min_value=5,max_value=20)
    slugfield = forms.SlugField()
    emailfield = forms.EmailField(min_length=10,max_length=15)
    urlfield = forms.URLField(min_length=10,max_length=15)
    #Customized fields
    passwordfield = forms.CharField(widget=forms.PasswordInput,max_length=15,min_length=5)
    descriptionfield = forms.CharField(widget=forms.Textarea)
    feedbackfield = forms.CharField(widget=forms.TextInput(attrs = {'class':'class1'}))
    notesfield = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':40}))