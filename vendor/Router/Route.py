# -*- coding: utf-8 -*-
from vendor.Contracts.Container import Container
from .Router import Router

class Route():
    
    # hungry Singleton Pattern
    def __init__(self, app: Container):
        #self.routers = [
        #   dict,
        #   router ojb,
        #   dict,
        #]
        self.app = app
        self.routers = []
        self.routers_http_method = {
            "GET":      {},
            "POST":     {},
            "DELETE":   {},
            "UPDATE":   {},
        }
        self.group_middle = []
        self.group_namespace = []
        self.group_prefix = []
        
    def match_router(self, url: str, http_method: str):
        router = None
        for obj in self.routers:
            if type(obj) is dict:
                if url in obj.keys():
                    router = obj[url]
            elif type(obj) is Router:
                if obj.match(url):
                    router = obj
        if not router:
            raise Exception('404')
        # match http method
        if router.http_method != http_method:
            if url not in self.routers_http_method[http_method].keys():
                raise Exception('404')
            else:
                return self.routers_http_method[http_method][url]
    
    def add(self, router: Router):
        if router.regular:
            self.routers.append(router)
        else:
            if type(self.routers[-1]) is list:
                self.routers[-1].append(router)
            else:
                self.routers.append([router])
        
        http_method = router.http_method
        self.routers_http_method[http_method][router.url] = router
        
    def group(self, middleware=None, namespace='', prefix=''):
        if middleware:
            self.group_middle.append(middleware)
        if namespace:
            self.group_namespace.append(namespace)
        if prefix:
            self.group_prefix.append(prefix)
        
    def get(self, url, reflect_obj_method):
        router = Router(url, reflect_obj_method, 'GET')
        self.add(router)
        return router

    def post(self, url, reflect_obj_method):
        router = Router(url, reflect_obj_method, 'POST')
        self.add(router)
        return router

    def delete(self, url, reflect_obj_method):
        router = Router(url, reflect_obj_method, 'DELETE')
        self.add(router)
        return router

    def update(self, url, reflect_obj_method):
        router = Router(url, reflect_obj_method, 'UPDATE')
        self.add(router)
        return router

    def dispatch(self, request):
        pass
        # todo
        