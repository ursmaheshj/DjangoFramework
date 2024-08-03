from cel_main import TaskQueue,WriteLog

TaskQueue.delay("First task for celery")

WriteLog.delay("Debugging log for celery")