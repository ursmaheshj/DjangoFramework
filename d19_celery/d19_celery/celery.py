import os
from time import sleep
from celery import Celery

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


# command to run docker container with redis client
# docker run -d --name redis-celery(container-name) -p 6379:6379 redis
# command to connect with redis docker client and run redis commands
# docker exec -it redis-celery sh > redis-cli > keys *