from multiprocessing import Process
from Queue import Queue


job = 0
q = Queue(maxsize=2)

def work():
    global job
    job = q.get()
    import time; time.sleep(8)
    print("Job done: {0}".format(job))

def my_view(request):
    global job
    if not q.full():
        job += 1
        q.put_nowait(job)
        print("Job submited: {0}".format(job))
        Process(target=work, args=(q,)).start()
    else:
        print("Queue is full")
    return {'project':'asyncapp'}
