#!/usr/bin/python
from gevent import wsgi
from views import get_fib, google_body_fetcher, store_service, paige404
from router import RouteDispatcher  

if __name__ == "__main__" :
    PORT = 8080
    address = "127.0.0.1"
    # Create Routes
    dispatch = RouteDispatcher()
    dispatch.register_route(r"^/fib/(?P<num>\d+)/?$", get_fib)
    dispatch.register_route(r"^/google-body/?$", google_body_fetcher)
    dispatch.register_route(r"^/store/?$", store_service)
    # start server
    print 'Serving at {} on {}...'.format(address, PORT)
    wsgi.WSGIServer((address, PORT), dispatch).serve_forever()
