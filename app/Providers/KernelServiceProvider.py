# -*- coding: utf-8 -*-
from vendor.Providers.ServiceProvider import ServiceProvider
from app.Http.Kernel import Kernel


# 简单的File服务提供者
class KernelServiceProvider(ServiceProvider):
    
    def register(self):
        def get_kernel():
            return Kernel()
        
        self.app.register('kernel', get_kernel)