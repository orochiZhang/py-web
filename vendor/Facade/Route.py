# -*- coding: utf-8 -*-
from .Facade import Facade


# File门面
class Route(metaclass=Facade):
    @staticmethod
    def get_facade_accessor():
        return 'route'
