from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name']='Ram'
    request.session['lname']='Raghuvanshi'
    return render(request,'app1/setsession.html')

def getsession(request):
    # name = request.session['name']
    # lname = request.session['lname']
    name = request.session.get('name')
    request.session.setdefault('age',25)
    lname = request.session.get('lname',"Lname not available")
    items = request.session.items()
    return render(request,'app1/getsession.html',{'name':name,'lname':lname,'items':items})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'app1/delsession.html')