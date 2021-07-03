# -*- coding: utf-8 -*-
from vendor.Facade.Route import Route

class RouteGroup():
    def __init__(self, middleware=None, namespace='', prefix=''):
        self.middleware = middleware
        self.namespace = namespace
        self.prefix = prefix
    
    def __enter__(self):
        Route().group(self.middleware, self.namespace, self.prefix)
        return Route()
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        Route().pop_group(self.middleware, self.namespace, self.prefix)

