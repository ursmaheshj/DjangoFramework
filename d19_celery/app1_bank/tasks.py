from celery import shared_task
from time import sleep

@shared_task
def sub_task(x,y):
    print("executing sub task")
    sleep(10)
    return x-y

@shared_task
def clear_session_cache(id):
    print(f'Session cache cleared:{id}')
    return id

@shared_task
def clear_redis_cache(id):
    print(f'Redis cache cleared:{id}')
    return id