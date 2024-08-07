from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask,IntervalSchedule
import json

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


#########Creating Periodic task for django beat
@shared_task
def clear_rabbitmq_data(id):
    print(f'RabbitMQ tasks cleared:{id}')
    return id

#creating schedule every 30 sec
schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period = IntervalSchedule.SECONDS,
)
#Scheduling Periodic task
PeriodicTask.objects.get_or_create(
    name = 'Clear RabbitMQ Periodic Task',
    task = 'app1_bank.tasks.clear_rabbitmq_data',
    interval = schedule,
    args = json.dumps(['hello']), #argument passed as json encoded string
)