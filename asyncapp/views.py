import time
from multiprocessing import Process
from asyncapp import running

def mi_funcion(running):
    if not running.value:
	running.value = 1
	print "Building..."
        import time; time.sleep(10)
        print "Hola chavales"
        running.value = 0
    else:
        print "Still building..."

def my_view(request):
    Process(target=mi_funcion, args=(running,)).start()
    return {'project':'asyncapp'}
