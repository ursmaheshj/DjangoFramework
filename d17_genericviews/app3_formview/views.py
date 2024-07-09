from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from app3_formview.forms import StudentForm

# Create your views here.
class StudentFormView(FormView):
    form_class = StudentForm
    template_name = 'app3_formview/studentform.html'
    success_url = '/thankyou/'
    initial = {'name':'Nikita','roll':45}
    def form_valid(self, form) -> HttpResponse:
        print(form)
        # return super().form_valid(form)
        print(form.cleaned_data())
        return HttpResponse('Data received')


class ThankYouTemplateView(TemplateView):
    template_name = 'app3_formview/thankyou.html'