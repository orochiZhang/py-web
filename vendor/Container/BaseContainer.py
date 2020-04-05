# -*- coding: utf-8 -*-
import vendor.Contracts.Kernel
import vendor.Contracts.Request
import vendor.Contracts.Router

# 容器基类
class BaseContainer(object):
    classMap = {}

    contractMap = {
        vendor.Contracts.Kernel.Kernel:     'kernel',
        vendor.Contracts.Request.Request:   'request',
        vendor.Contracts.Router.Router:     'router',
    }

    @classmethod
    def register(cls, name, func):
        pass

    @classmethod
    def make(cls, name):
        pass
