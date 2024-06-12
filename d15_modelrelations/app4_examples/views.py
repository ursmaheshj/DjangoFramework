from django.shortcuts import render
from app4_examples.models import User,Page,Post,Song

# Create your views here.
def home(request):
    return render(request,'app4_examples/home.html')

def user(request):
    users = User.objects.all()
    userswithm = User.objects.filter(username__startswith='m')
    userson12 = User.objects.filter(page__publish = '2024-06-12')
    usersinpython = User.objects.filter(post__publish_in__pagename = 'Python')
    users4min = User.objects.filter(song__duration = 4)
    context = {
        'users':users,
        'userswithm':userswithm,
        'userson12':userson12,
        'usersinpython':usersinpython,
        'users4min':users4min,
    }
    return render(request,'app4_examples/user.html',context)

def page(request):
    return render(request,'app4_examples/page.html')

def post(request):
    return render(request,'app4_examples/post.html')

def song(request):
    return render(request,'app4_examples/song.html')
