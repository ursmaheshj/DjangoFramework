from celery import Celery
import time

# app = Celery('cel_main',broker='pyamqp://')
app = Celery('cel_main', backend='rpc://',broker='pyamqp://')

@app.task
def TaskQueue(message):
    time.sleep(10)
    print(f"TaskQueue: {message}")
    return "TASK ADDED"

@app.task
def WriteLog(log):
    print(f"Log: {log}")
    return "LOG WRITTEN"



#celery -A cel_main worker --loglevel=INFO
#celery -A cel_main worker --loglevel=INFO -P solo 
##solo runs task single-threaded instead of parallel
#celery -A cel_main worker --concurrency=2 --loglevel=INFO -P solo
##concurrency flag denotes the workers to be initiated
#celery -A cel_main worker --concurrency=2 --loglevel=INFO --without-gossip --without-mingle --without-heartbeat -Ofair #doestnt work 