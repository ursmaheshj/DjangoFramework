from celery import shared_task
from time import sleep

@shared_task
def sub_task(x,y):
    print("executing sub task")
    sleep(10)
    return x-y