from cel_main import TaskQueue,WriteLog

result = TaskQueue.delay("First task for celery")
# result = TaskQueue.apply_async(("First task for celery",),queue='second')  #using apply_async to give queue name
print(result.get())

print(WriteLog.delay("Debugging log for celery").get())