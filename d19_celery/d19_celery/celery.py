import os
from time import sleep
from celery import Celery
from datetime import timedelta
from celery.schedules import crontab,solar

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'd19_celery.settings')

app = Celery('d19_celery')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

#Default Task
# @app.task(bind=True, ignore_result=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# @app.task
@app.task(name="MyTaskName")
def add_task(x,y):
    print("executing add task")
    sleep(10)
    return x+y

app.conf.beat_schedule = {
    'SESSION_CLEAR_EVERY10SEC':{
        'task':'app1_bank.tasks.clear_session_cache',
        # 'schedule':20,   
        # 'schedule':solar('sunset',-37.65,144.546), #Scheduling using solar/based on sunset,sunrise,longitude,altitude  
        # 'schedule':crontab(minute='*/1'),   #scheduling using crontab
        'schedule':timedelta(seconds=30),  #scheduling using timedelta
        'args':('101',),
    },
    # more scheduled tasks can be added here
}

### Command to run Celery worker 
# celery -A app_name worker -l info -P solo
### Command to run celery beat
# celery -A app_name beat -l info
### command to run docker container with redis client
# docker run -d --name redis-celery(container-name) -p 6379:6379 redis
### command to connect with redis docker client and run redis commands
# docker exec -it redis-celery sh > redis-cli > keys *
### command to run docker container with rabbitMQ client
# docker run -p 15672:15672 -p 5672:5672 --restart=no -d rabbitmq:management