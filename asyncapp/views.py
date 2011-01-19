from multiprocessing import Process, Lock, Queue


job = 0
q = Queue(maxsize=3)
lock = Lock()

def work():
    import time; time.sleep(8)
    job = q.get()
    print("Job done: {0}".format(job))
    print("Queue size: {0}\n".format(q.qsize()))
    if not q.empty():
        work()
    else:
        lock.release()

def my_view(request):
    global job
    if not q.full():
        job += 1
        q.put_nowait(job)
        # Not running
        if lock.acquire(False):
            Process(target=work).start()
            print("Job {0} submitted and working on it".format(job))
        else:
            print("Job {0} submitted while working".format(job))
    else:
        print("Queue is full")
    print("Queue size: {0}\n".format(q.qsize()))
    return {'project':'asyncapp'}
