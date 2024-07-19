from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required,user_passes_test

# Create your views here.

def staff_member_required(user):
    return user.is_staff
# @login_required   #Makes sure user is logged in otherwise redirect to login
# @permission_required('app1_funcauthview.add_blog')  #if user have given permission then only executes the view
@user_passes_test(staff_member_required)
def profile(request):
    return render(request,'registration/profile.html')