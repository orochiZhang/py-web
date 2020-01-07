# -*- coding: utf-8 -*-


# 容器基类
class BaseContainer(object):
    classMap = {}

    @classmethod
    def register(cls, name, func):
        pass

    @classmethod
    def make(cls, name):
        pass
