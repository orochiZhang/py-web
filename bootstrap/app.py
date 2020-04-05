# -*- coding: utf-8 -*-
from config.app import config
from vendor.Container.Container import Container

if 'app' not in globals():
    app = None

def get_application():
    global app
    if app:
        return app
    app = Container()
    app.register_module(config['providers'])
    app.set_facade_application(config['aliases'])
    return app

def init_application():
    global app
    app = Container()
    app.register_module(config['providers'])
    app.set_facade_application(config['aliases'])
    app.boot()