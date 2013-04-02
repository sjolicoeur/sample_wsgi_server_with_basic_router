import re
from views import paige404

class RouteDispatcher(object):
    """ 
        Main point of entry for our WSGI app to resolve and register url pattern paths.
        Routes will be executed based on the first route matched. 
        to register a url that will resolve /hello/john

        >>> def foo(env, start_response, name) : 
        ...     print name 
        ...     start_response('200 OK', [('Content-Type', 'text/html')])
        ...     return ["hello {}".format(name)]
        ...
        >>> router =  RouteDispatcher()
        >>> router.register_route(r"/hello/(?P<name>\w+)/?", foo)
    """
    def __init__(self):
        self.routes = {}

    def __call__(self, environ, start_response):
        requested_path = environ.get('PATH_INFO', "/" )
        try :

            controller, args = self.match_path_to_route(requested_path)
            return controller(environ, start_response, **args)
        except :
            import sys
            print "an error occured!!!"
            print sys.exc_info()
            return paige404(environ, start_response)

    def match_path_to_route(self, path_to_route):
        for route_pattern, controller in self.routes.items() :
            found_match = re.match(route_pattern, path_to_route)
            if found_match :
                extracted_args = found_match.groupdict()
                return controller, extracted_args
        raise Exception("Route not found")

    def register_route(self, path, func):
        self.routes[path] = func  