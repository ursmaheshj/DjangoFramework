from django.shortcuts import render

# Create your views here.
def setcookie(request):
    response = render(request,'app1/setcookie.html')
    response.set_cookie('Name','ram')
    response.set_cookie('age',28)
    response.set_cookie('12',28)
    return response

def getcookie(request):
    cookies = request.COOKIES
    # name = request.COOKIES['age']
    name = request.COOKIES.get('Name')
    return render(request,'app1/getcookie.html',{'cookies':cookies,'name':name})

def deletecookie(request):
    response = render(request,'app1/deletecookie.html')
    response.delete_cookie('Name')
    return response