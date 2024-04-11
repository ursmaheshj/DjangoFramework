from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Ram'
    request.session['lname']='Raghuvanshi'
    request.session.set_expiry(5)
    return render(request,'app1/setsession.html')

def getsession(request):
    # name = request.session['name']
    # lname = request.session['lname']
    print(request.session.get_session_cookie_age()) 
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.get_expire_at_browser_close())
    name = request.session.get('name')
    # request.session.setdefault('age',25)
    lname = request.session.get('lname',"Lname not available")
    items = request.session.items()
    return render(request,'app1/getsession.html',{'name':name,'lname':lname,'items':items})

def delsession(request):
    # if 'name' in request.session:
    #     del request.session['name']
    request.session.flush()
    request.session.clear_expired()
    return render(request,'app1/delsession.html')