# -*- coding: utf-8 -*-
from .ServiceProvider import ServiceProvider
from vendor.Foundation.Http.Request import Request


# a Simple Request ServiceProvider
class RequestServiceProvider(ServiceProvider):

    def register(self):
        def get_request(env):
            return Request(env)

        self.app.register('request', get_request)