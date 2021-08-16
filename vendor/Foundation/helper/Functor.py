# -*- coding: utf-8 -*-


class Functor(object):
    
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def __call__(self, *args, **kwargs):
        self.args = list(self.args).extend(args)
        self.kwargs.update(kwargs)
        self.func(*args, **kwargs)