# -*- coding: utf-8 -*-

class TestMiddleware():
    """
    
    """
    #TestMiddleware
    # @param  \Illuminate\Http\Request  $request
    # @param  \Closure  $next
    # @param  string|null  $guard
    # @return mixed
    def handle(self, request, next_closure, guard=None):
        """
        @param request: vendor.Http.Request
        @param next_closure:
        @param guard: string|None
        @return:
        """
        print('Test Middleware')
        return next_closure(request)
