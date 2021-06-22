# -*- coding: utf-8 -*-
from vendor.Facade.Route import Route

def init():
    Route().post('/home', 'HomeController@test')