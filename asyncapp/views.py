from multiprocessing import Lock, Process

lock = Lock()
acquired = False

def mi_funcion():
    global acquired
    if not acquired:
        acquired = lock.acquire()
        print "Building..."
        import time; time.sleep(10)
        print "Hola chavales"
        acquired = lock.release()
    else:
        print "Still building..."

def my_view(request):
    Process(target=mi_funcion).start()
    return {'project':'asyncapp'}
