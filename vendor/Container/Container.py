# -*- coding: utf-8 -*-
from .BaseContainer import BaseContainer


# 容器类
class Container(BaseContainer):

    @classmethod
    def register(cls, name, func):
        if name not in cls.classMap.keys():
            cls.classMap[name] = func

    @classmethod
    def make(cls, name, parameter=None):
        if name in cls.contractMap:
            name = cls.contractMap[name]
        if name in cls.classMap:
            if parameter:
                return cls.classMap[name](*parameter)
            else:
                return cls.classMap[name]()
        else:
            raise Exception('Facade %s not register' % name)

    def register_module(self, providers):
        import importlib

        for c, m in providers.items():
            module = importlib.import_module(m)
            getattr(module, c)(self).register()

    def set_facade_application(self, aliases):
        import importlib

        for c, m in aliases.items():
            module = importlib.import_module(m)
            getattr(module, c).set_facade_application(self)
            
    def boot(self):
        for name, provider in self.classMap.items():
            self.boot_provider(provider)
            
    def boot_provider(self, provider):
        if hasattr(provider, 'boot'):
            return getattr(provider, 'boot')()
