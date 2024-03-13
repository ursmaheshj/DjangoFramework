from django.shortcuts import render

# Create your views here.
def home(request,check):
    return render(request,'app3/home.html',{'check':check})

def details(request,details_id=1):
    context = {
        'page_info':'Details Page',
        'details':details_id
    }
    return render(request,'app3/details.html',context)

def subdetails(request,details_id,subdetails_id):
    context = {
        'page_info':'Sub Details Page',
        'details':details_id,
        'subdetails':subdetails_id,
    }
    return render(request,'app3/details.html',context)