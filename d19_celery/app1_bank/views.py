from django.shortcuts import render
from d19_celery.celery import add_task
from app1_bank.tasks import sub_task
from celery.result import AsyncResult

# Create your views here.
def home(request):
    return render(request,'app1_bank/index.html')

def about(request):
    return render(request,'app1_bank/about.html')

def getBalance(request):
    # task_id1 = add_task.delay(20,30) #enque task using delay()
    task_id1 = sub_task.apply_async(args=(20,30)) #enque task using apply_async()
    print(task_id1.ready())
    print(task_id1.successful())
    print(task_id1.failed())
    print(task_id1)
    # print(task_id2)
    return render(request,'app1_bank/balance.html',{'task_id':task_id1})

def getResult(request,task_id):
    task = AsyncResult(task_id)
    return render(request,'app1_bank/result.html',{'task':task})