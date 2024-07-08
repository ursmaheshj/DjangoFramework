from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView
from app1_listview.models import Student

# Create your views here.
class StudentListView(ListView):
    model = Student
    # template_name_suffix = '_get'     #Custom suffix instead of _list use _get
    template_name = 'app1_listview/student_list.html'      #Custom template name
    # context_object_name = 'students'    #Custom context name
    ordering = ['-name']

    def get_queryset(self) -> QuerySet[Any]:
        return Student.objects.filter(course='love')  #it will return only those students with course as love
    
    def get_context_data(self, **kwargs) -> dict[str, Any]:  #updates context variable along with new data
        context = super().get_context_data(**kwargs)
        context["freshers"] = Student.objects.all().order_by('name')
        return context
    
    def get_template_names(self) -> list[str]:  #If cookie has user=ram it will render ram.html template
        template_name = self.template_name
        try:
            if self.request.COOKIES['user']=='ram':
                template_name = f'app1_listview/{self.request.COOKIES['user']}.html'
        except Exception as e:
            print(e)
        
        return [template_name]