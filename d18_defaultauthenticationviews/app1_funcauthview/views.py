from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
# @login_required   #Makes sure user is logged in otherwise redirect to login
@permission_required('app1_funcauthview.add_blog')
def profile(request):
    return render(request,'registration/profile.html')