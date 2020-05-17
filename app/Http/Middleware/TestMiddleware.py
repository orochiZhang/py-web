# -*- coding: utf-8 -*-

def Closure():
    pass

class TestMiddleware():

    #TestMiddleware
    #@param  \Illuminate\Http\Request  $request
    #@param  \Closure  $next
    #@param  string|null  $guard
    #@return mixed
    def handle(self, request,  next_closure: Closure, guard=None):
        print('Test Middleware')
        return next_closure(request)
