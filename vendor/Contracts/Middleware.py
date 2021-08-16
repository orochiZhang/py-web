# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class Middleware(ABC):
    
    @abstractmethod
    def handle(self, request, next_closure, guard=None):
        """
        @param request: vendor.Http.Request
        @param next_closure: vendor.Contracts.Closure
        @param guard: string|null
        @return: mixed
        """
        return next_closure(request)