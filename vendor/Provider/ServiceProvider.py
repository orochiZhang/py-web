# -*- coding: utf-8 -*-


# 服务提供者基类
class ServiceProvider(object):

    def __init__(self, app):
        self.app = app

    '''
     * Get the registered name of the class.
     *
     * @return a class instance
    '''

    @staticmethod
    def register():
        pass
