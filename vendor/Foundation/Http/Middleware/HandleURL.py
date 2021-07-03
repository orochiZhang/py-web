# -*- coding: utf-8 -*-
from vendor.Contracts.Middleware import Middleware
from vendor.Contracts.Request import Request

class HandleURL(Middleware):
    
    except_key = []

    def handle(self, request, next_closure, guard=None):
        """
        @param request: vendor.Http.Request
        @param next_closure: vendor.Contracts.Closure
        @param guard: string|null
        @return: mixed
        """
        url = request.url
        if not url.endswith('/'):
            url += '/'
        request.url = url.replace('//', '/')
        return next_closure(request)