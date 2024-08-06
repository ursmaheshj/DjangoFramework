from django.shortcuts import render
from d19_celery.celery import add_task
from app1_bank.tasks import sub_task

# Create your views here.
def home(request):
    return render(request,'app1_bank/index.html')

def about(request):
    return render(request,'app1_bank/about.html')

def getBalance(request):
    result1 = add_task.delay(20,30) #enque task using delay()
    result2 = sub_task.apply_async(args=(20,30))
    print(result1)
    print(result2)
    return render(request,'app1_bank/balance.html')