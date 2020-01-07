# -*- coding: utf-8 -*-
from .Facade import Facade


# File门面
class File(metaclass=Facade):
    @staticmethod
    def get_facade_accessor():
        return 'files'
