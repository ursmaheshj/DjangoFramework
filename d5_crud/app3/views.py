from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'app3/home.html')

def details(request,details_id):
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