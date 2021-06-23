# -*- coding: utf-8 -*-
from vendor.Contracts.Kernel import Kernel as KernelContract
from vendor.Pipeline.Pipeline import Pipeline
from vendor.Exception.Exception import PageNotFoundError, MethodNotAllowError
from werkzeug.wrappers import Response

class Kernel(KernelContract):
    # The application's global HTTP middleware stack.
    # These middleware are run during every request to your application.
    # @var array
    middleware = []
    
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
    
    def handle(self, request):
        """
        Handle an incoming HTTP request.
        @param request: vendor.Http.Request
        @return: vendor.Http.esponse
        """
        try:
            response = self.send_request_through_router(request)
        except PageNotFoundError:
            response = Response("404", 404)
        except MethodNotAllowError:
            response = Response("405", 405)
        
        return response
    
    def send_request_through_router(self, request):
        """
        Send the given request through the middleware / router.
        @param request: vendor.Http.Request
        @return: vendor.Http.Response
        """
        self.app.instance('request', request)
        middleware = self.middleware[:]
        return (Pipeline(self.app)).send(request) \
            .through(middleware) \
            .then(self.dispatch_to_router)
    
    def dispatch_to_router(self, request):
        """
        search router by request url.
        @param request: vendor.Http.Request
        @return: vendor.Http.Response
        """
        self.app.instance('request', request)
        return self.route.dispatch(request)