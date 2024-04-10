from django.shortcuts import render

# Create your views here.
def ssetcookie(request):
    response = render(request,'app2/ssetcookie.html')
    response.set_signed_cookie('Name','ram',salt='django')
    response.set_signed_cookie('age',28)
    return response

def sgetcookie(request):
    name = request.get_signed_cookie('Name',default='Not found',salt='django')
    age = request.get_signed_cookie('age',default='Not found')
    return render(request,'app2/sgetcookie.html',{'name':name,'age':age})

def sdeletecookie(request):
    response = render(request,'app2/sdeletecookie.html')
    response.delete_cookie('Name')
    return response