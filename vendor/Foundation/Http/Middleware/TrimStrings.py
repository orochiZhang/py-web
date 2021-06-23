# -*- coding: utf-8 -*-
from vendor.Contracts.Middleware import Middleware

class TrimStrings(Middleware):
    
    except_key = []

    def handle(self, request, next_closure, guard=None):
        """
        @param request: vendor.Http.Request
        @param next_closure: vendor.Contracts.Closure
        @param guard: string|null
        @return: mixed
        """
        print(type(request))
        for key in self.except_key:
            if request.has_parameter(key):
                content = request.get_parameter(key).strip()
                request.set_parameter(key, content)
        return next_closure(request)