from multiprocessing import Process, Queue


job = 0
q = Queue(maxsize=2)
p = Process()

def work():
    global p
    import time; time.sleep(8)
    job = q.get()
    print("Job done: {0}".format(job))
    if q.qsize > 0:
        p = Process(target=work)
        p.start()

def my_view(request):
    global job
    if not q.full():
        job += 1
        q.put_nowait(job)
        global p
        if not p.is_alive():
            p = Process(target=work)
            p.start()
        print("Job submitted: {0}".format(job))
    else:
        print("Queue is full")
    return {'project':'asyncapp'}
