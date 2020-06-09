# -*- coding: utf-8 -*-
from app.Http.Middleware.TestMiddleware import TestMiddleware
from vendor.Pipeline.Pipeline import Pipeline

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
        response = self.sendRequestThroughRouter(request)
        # try:
        #     # request.enableHttpMethodParameterOverride()
        #
        #     response = self.sendRequestThroughRouter(request)
        # except:
        #     response = None
            # self.reportException(e)
            # response = self.renderException(request, e)
        # except Throwable e:
        #     self.reportException(e = new FatalThrowableError(e))
        #
        #     response = self.renderException(request, e)
        # }

        # self.app['events'].dispatch(
        #     new Events\RequestHandled(request, response)
        # )
        return response

    # Send the given request through the middleware / router.
    # @param  \Illuminate\Http\Request  request
    # @return \Illuminate\Http\Response

    def sendRequestThroughRouter(self, request):
        self.app.instance('request', request)

        # Facade::clearResolvedInstance('request')

        # self.bootstrap()
        # if self.app.shouldSkipMiddleware():
        #     middleware = []
        # else:
        #     middleware = self.middleware
        middleware = self.middleware
        return (Pipeline(self.app)).send(request)\
                    .through(middleware)\
                    .then(self.dispatchToRouter())
    
    def dispatchToRouter(self):
        def function(request):
            nonlocal self
            self.app.instance('request', request)
            return self.route.dispatch(request)
        return function