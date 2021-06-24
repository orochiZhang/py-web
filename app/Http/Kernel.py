# -*- coding: utf-8 -*-
from app.Http.Middleware.TestMiddleware import TestMiddleware
from app.Http.Middleware.TrimStrings import TrimStrings
from vendor.Foundation.Http.Kernel import Kernel as BaseKernel

class Kernel(BaseKernel):
    
    # The application's global HTTP middleware stack.
    # These middleware are run during every request to your application.
    # @var array
    middleware = [
        TestMiddleware,
        TrimStrings
    ]
    
    # The application's route middleware groups.
    # @ var dict
    middlewareGroups = {}

