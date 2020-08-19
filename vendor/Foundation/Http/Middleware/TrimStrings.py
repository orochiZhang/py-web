# -*- coding: utf-8 -*-

class TrimStrings():
    
    except_key = []

    #TestMiddleware
    #@param  \Illuminate\Http\Request  $request
    #@param  \Closure  $next
    #@param  string|null  $guard
    #@return mixed
    def handle(self, request,  next_closure, guard=None):
        
        return next_closure(request)