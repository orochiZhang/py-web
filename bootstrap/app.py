# -*- coding: utf-8 -*-
from vendor.Container.Container import Container
from vendor.Router.Route import Route as RouteSingleton

from app.Http.RouteBoot import RouteBoot
from config.app import config


def get_application():
    app = Container()
    return app

def boot():
    app = Container()
    app.register_module(config['providers'])
    app.set_facade_application(config['aliases'])
    app.boot()
    app.singleton('route', RouteSingleton(app))
    RouteBoot().boot()

