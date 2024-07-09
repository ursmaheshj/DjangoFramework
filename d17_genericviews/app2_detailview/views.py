from typing import Any
from django.shortcuts import render
from django.views.generic.detail import DetailView
from app2_detailview.models import Dstudent

# Create your views here.
class StudentDetailView(DetailView):
    model = Dstudent
    # template_name = 'app2_detailview/dstudent.html' #Custom template name
    # context_object_name = 'studentdetails'  #Custom context name
    # pk_url_kwarg = 'id'  #can be used instead of pk in urls

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['all_student'] = self.model.objects.all()
        return context