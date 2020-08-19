# -*- coding: utf-8 -*-
from vendor.Providers.ServiceProvider import ServiceProvider


# 简单的File服务提供者
class RouteServiceProvider(ServiceProvider):
    
    def register(self):
        def get_route():
            return self.app.get_singleton('Route')
    
        self.app.register('route', get_route)