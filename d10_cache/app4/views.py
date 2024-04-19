from django.shortcuts import render
from django.core.cache import cache

# Create your views here.
# def lowlevelhome(request):
#     if cache.get('Name','Not Exist') == 'Not Exist':
#         cache.set('Name','fs',15)
#     data = cache.get('Name')
#     return render(request,'app4/home.html',{'data':data})

# def lowlevelhome(request):
#     data = cache.get_or_set('Name','Ram',30)
#     return render(request,'app4/home.html',{'data':data})

def lowlevelhome(request):
    kvs = {'Name':'Krishna','Age':0,'City':'Dwarka'}
    cache.set_many(kvs,60)
    data = cache.get_many(kvs)
    return render(request,'app4/home.html',{'data':data})

def lowlevelgethome(request):
    keys = ['Name','Age']
    data = cache.get_many(keys)
    # cache.incr('Age',delta=5)
    cache.decr('Age',delta=5)
    # cache.delete('Name',version=2)
    # cache.delete_many(['Name','Age','roll'])
    return render(request,'app4/home.html',{'data':data})
