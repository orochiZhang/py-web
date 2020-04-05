# -*- coding: utf-8 -*-

class Kernel(object):
    
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