from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import ContactForm

# Create your views here.
class Demo(View):         
    name = 'Mahesh'
    def get(self,request):
        return HttpResponse(f'<h2>Class Based View | name:{self.name}</h2>')
    
class DemoChild(Demo):
    # it will inherit the get method from parent class Demo
    pass 

class Demotemplate(View):
    def get(self,request):
        context = {'name':'Ramesh'}
        return render(request,'app1/demotemplate.html',context)
    
class ContactView(View):
    form = ContactForm()
    def get(self,request):
        return render(request,'app1/contact.html',{'form':self.form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['name']
        else: 
            data = 'Invalid data'
        return render(request,'app1/contact.html',{'form':self.form,'data':data})
    
class NewsChannel(View):
    template_name = ''
    def get(self,request):
        return render(request,self.template_name)