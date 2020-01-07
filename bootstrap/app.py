# -*- coding: utf-8 -*-
from config.app import config
from vendor.Container.Container import Container


def get_application():
    app = Container()
    app.register_module(config['providers'])
    app.set_facade_application(config['aliases'])
    return app
