# -*- coding: utf-8 -*-
from vendor.Contracts.Middleware import Middleware as MiddlewareContract


class TestMiddleware(MiddlewareContract):

    def handle(self, request, next_closure, guard=None):
        """
        @param request: vendor.Http.Request
        @param next_closure: vendor.Contracts.Closure
        @param guard: string|None
        @return: mixed
        """
        print('Test Middleware')
        return next_closure(request)
