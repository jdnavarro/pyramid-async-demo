from multiprocessing import Process
from asyncapp import queue

def mi_funcion(queue):
    queue.put_nowait("Building...")
    try:
        import time; time.sleep(8)
	queue.get()
	queue.put_nowait("Hola Chavales")
    except:
        pass
    
def my_view(request):
    if queue.empty():
        Process(target=mi_funcion, args=(queue,)).start()
    	print "Building..."
    else:
        print queue.get()
    return {'project':'asyncapp'}
