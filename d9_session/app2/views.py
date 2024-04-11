from django.shortcuts import render

# Create your views here.
def set_test_cookie(request):
    request.session.set_test_cookie()
    return render(request,'app2/settestcookie.html')

def check_test_cookie(request):
    cookie_allowed = request.session.test_cookie_worked()
    return render(request,'app2/checktestcookie.html',{'cookie_allowed':cookie_allowed})

def del_test_cookie(request):
    request.session.delete_test_cookie()
    return render(request,'app2/deltestcookie.html')