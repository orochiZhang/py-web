# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import vendor.Contracts.Kernel
import vendor.Contracts.Request
import vendor.Contracts.Router

# Container Contracts
class Container(object):
    
    def __init__(self):
        self.class_map = {}
        self.contract_map = {
            vendor.Contracts.Kernel.Kernel:     'kernel',
            vendor.Contracts.Request.Request:   'request',
            vendor.Contracts.Router.Router:     'router',
        }

    @abstractmethod
    def register(self, name, func):
        pass

    @abstractmethod
    def make(self, name):
        pass
