# -*- coding: utf-8 -*-
from app.Http.Middleware.TestMiddleware import TestMiddleware
from vendor.Pipeline.Pipeline import Pipeline
from vendor.Exception.Exception import PageNotFoundError
from werkzeug.wrappers import Response

class Kernel(object):
    
    # The application's global HTTP middleware stack.
    # These middleware are run during every request to your application.
    # @var array
    middleware = [
        TestMiddleware
    ]
    
    # The application's route middleware groups.
    # @ var dict
    middlewareGroups = {}
    
    
    # The application's route middleware.
    # These middleware may be assigned to groups or used individually.
    # @ var dict
    routeMiddleware = {}
    
    def __init__(self, app, route):
        self.app = app
        self.route = route
        
    # Handle an incoming HTTP request.
    #
    # @param  \Illuminate\Http\Request  request
    # @return \Illuminate\Http\Response
    def handle(self, request):
        try:
            response = self.sendRequestThroughRouter(request)
        except PageNotFoundError:
            response = Response("404", 404)

        return response

    # Send the given request through the middleware / router.
    # @param  \Illuminate\Http\Request  request
    # @return \Illuminate\Http\Response

    def sendRequestThroughRouter(self, request):
        self.app.instance('request', request)
        middleware = self.middleware[:]
        return (Pipeline(self.app)).send(request)\
                    .through(middleware)\
                    .then(self.dispatchToRouter())
    
    def dispatchToRouter(self):
        def function(request):
            nonlocal self
            self.app.instance('request', request)
            return self.route.dispatch(request)
        return function