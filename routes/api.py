# -*- coding: utf-8 -*-
from vendor.Facade.Route import Route
from .RouteGroup import RouteGroup

def init():
    Route().get('/', 'HomeController@test2')
    with RouteGroup(prefix='test') as router:
        router.get('/', 'HomeController@test2')
    Route().get('/home', 'HomeController@test')