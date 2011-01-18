from multiprocessing import Process, Lock, Queue, Value


job = 0
q = Queue(maxsize=2)
lock = Lock()
running = Value('B', 0)

def work():
    global job
    import time; time.sleep(8)
    job = q.get()
    print("Job done: {0}".format(job))
    print(q.qsize())
    if not q.empty():
        work()
    else:
        running.value = 0

def my_view(request):
    global job
    if not q.full() and not running.value:
        job += 1
        q.put_nowait(job)
        print("Job {0} submitted and working on it".format(job))
        if not running.value:
            running.value = 1
            Process(target=work).start()
    elif not q.full():
        job += 1
        q.put_nowait(job)
        print("Job {0} submitted while working".format(job))
    else:
        print("Queue is full")
    print(q.qsize())
    return {'project':'asyncapp'}
