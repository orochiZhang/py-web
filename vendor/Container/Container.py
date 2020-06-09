# -*- coding: utf-8 -*-
from vendor.Contracts.Container import Container as ContainerContract
import inspect
import importlib

class Container(ContainerContract):
    
    def __init__(self):
        self.instance_map = {}
        self.singleton_map = {}
        super(Container, self).__init__()

    def register(self, name, func):
        if name not in self.class_map.keys():
            self.class_map[name] = func
    
    def make_obj(self, name:str, parameter=None):
        m, c = 'app.Http.Controller.'+name, name
        module = importlib.import_module(m)
        if parameter:
            return getattr(module, c)(parameter)
        else:
            return getattr(module, c)()
    
    # todo 注意传入参数少过需要的参数的情况
    def make(self, name, parameter=None):
        if name in self.singleton_map:
            return self.get_singleton(name)
        if name in self.contract_map:
            name = self.contract_map[name]
        if name in self.class_map:
            if parameter:
                return self.class_map[name](*parameter)
            else:
                return self.reflect(self.class_map[name])
        else:
            raise Exception('Facade %s not register' % name)
    
    def reflect(self, object, parameter=None):
        arg_list = self.get_extenders(object)
        return object(*arg_list)
    
    def get_extenders(self, object):
        # get __init__ function arg
        arg_spec = inspect.getfullargspec(object.__init__)

        # new arg class and add to arg_list
        arg_list = []
        if not arg_spec.args:
            return arg_list
        for key in arg_spec.args:
            if key in arg_spec.annotations:
                arg_list.append(self.reflect(arg_spec.annotations[key]))
            elif arg_spec.defaults:
                arg_list.extend(arg_spec.defaults)
        return arg_list

    def register_module(self, providers):
        for c, m in providers.items():
            module = importlib.import_module(m)
            getattr(module, c)(self).register()

    def set_facade_application(self, aliases):
        for c, m in aliases.items():
            module = importlib.import_module(m)
            getattr(module, c).set_facade_application(self)
            
    def boot(self):
        for name, provider in self.class_map.items():
            self.boot_provider(provider)
            
    def boot_provider(self, provider):
        if hasattr(provider, 'boot'):
            return getattr(provider, 'boot')()

    def instance(self, name, obj):
        self.instance_map[name] = obj
        
    def singleton(self, name, obj):
        self.singleton_map[name] = obj
    
    def get_singleton(self, name):
        return self.singleton_map.get(name, None)
    