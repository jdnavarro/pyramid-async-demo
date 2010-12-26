from multiprocessing import Queue

from pyramid.config import Configurator
from asyncapp.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.add_view('asyncapp.views.my_view',
                    context='asyncapp:resources.Root',
                    renderer='asyncapp:templates/mytemplate.pt')
    config.add_static_view('static', 'asyncapp:static')
    return config.make_wsgi_app()

queue = Queue(maxsize=1)
