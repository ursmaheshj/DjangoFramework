from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def lowlevelhome(request):
#     if cache.get('Name','Not Exist') == 'Not Exist':
#         cache.set('Name','fs',15)
#     data = cache.get('Name')
#     return render(request,'app4/home.html',{'data':data})

def lowlevelhome(request):
    data = cache.get_or_set('Name','Ram',30)
    return render(request,'app4/home.html',{'data':data})

def lowlevelgethome(request):
    data = cache.get('Name','Not exist')
    return render(request,'app4/home.html',{'data':data})
