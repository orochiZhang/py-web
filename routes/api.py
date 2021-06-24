# -*- coding: utf-8 -*-
from vendor.Facade.Route import Route


def init():
    Route().get('/home', 'HomeController@test')
    Route().get('/', 'HomeController@test2')
