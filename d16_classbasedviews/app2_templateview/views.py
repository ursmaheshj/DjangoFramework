from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class MyTemplateView(TemplateView):
    template_name = 'app2/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = 'Ram'
        context["city"] = 'Ayodhya'
        try:
            context['class'] = kwargs['cl']  #getting kwargs provided in url and adding to context
        except:
            pass
        # context = {        #Using dictionary for context but it will effect extra_context
        #     'name':'Ram',
        #     'city':'Ayodhya',
        # }
        return context
    

