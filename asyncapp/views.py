from multiprocessing import Value, Process

alive = Value('B', 0)

def mi_funcion():
        print "Build started"
        import time; time.sleep(10)
        print "Hola chavales"
        alive.value = False

def my_view(request):
    if not alive.value:
        alive.value = True
        Process(target=mi_funcion).start()
    else:
        print("Still building...")
    return {'project':'asyncapp'}
