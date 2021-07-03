# -*- coding: utf-8 -*-


# 门面元类
class Facade(type):

    
    app = None

    @staticmethod
    def get_facade_accessor() -> str:
        """
        Get the registered name of the component.
        @return: string
        """
        return ''

    @classmethod
    def set_facade_application(mcs, app):
        mcs.app = app

    def __call__(cls, *args, **kwargs):
        if cls.app is None:
            raise Exception('no Container')
        return cls.app.make(cls.get_facade_accessor())
