# -*- coding: utf-8 -*-

class Router():
    
    
    def __init__(self, url, reflect_obj_method, http_method, id):
        self.regular = False
        self.url = url
        self.http_method = http_method
        self.middleware = []
        self.reflect_obj_method = reflect_obj_method
        self.ID = id
        
    def middleware(self, *args):
        self.middleware.extend(args)
