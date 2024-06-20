from typing import Any
from django.shortcuts import render
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.

class MyRedirectView(RedirectView):
    pattern_name='mindex'
    permanent = True #change status code from 301 to 302 indicating permanent redirect
    query_string = True

    def get_redirect_url(self, *args: Any, **kwargs: Any) -> str | None:
        print(kwargs)
        kwargs['pk']=45
        return super().get_redirect_url(*args, **kwargs)
    