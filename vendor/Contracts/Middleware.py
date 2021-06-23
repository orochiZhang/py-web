# -*- coding: utf-8 -*-

class Middleware(object):
    
    def handle(self, request, next_closure, guard=None):
        """
        @param request: vendor.Http.Request
        @param next_closure: vendor.Contracts.Closure
        @param guard: string|null
        @return: mixed
        """
        return next_closure(request)