# -*- coding: utf-8 -*-

config = {
    'providers': {
        'FileServiceProvider':      'vendor.Providers.FileServiceProvider',
        'RequestServiceProvider':   'vendor.Providers.RequestServiceProvider',
        'KernelServiceProvider':    'app.Providers.KernelServiceProvider',
        'RouteServiceProvider':     'app.Providers.RouteServiceProvider',
    },

    'aliases': {
        'File': 'vendor.Facade.File',
        'Route': 'vendor.Facade.Route',
    }
}