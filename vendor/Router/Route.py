# -*- coding: utf-8 -*-
from vendor.Contracts.Container import Container
from vendor.Pipeline.Pipeline import Pipeline
from vendor.Exception.Exception import PageNotFoundError, MethodNotAllowError
from .Router import Router

class Route():
    
    # hungry Singleton Pattern
    def __init__(self, app: Container):
        self.last_id = 0
        self.app = app
        self.routers = {
            "GET":      {},
            "POST":     {},
            "DELETE":   {},
            "UPDATE":   {},
        }
        self.regular_routers = {
            "GET":      [],
            "POST":     [],
            "DELETE":   [],
            "UPDATE":   [],
        }
        
        self.group_middle = []
        self.group_namespace = []
        self.group_prefix = []
        
    def match_router(self, url: str, http_method: str) -> Router:
        router = self.routers[http_method].get(url, None)
        
        for obj in self.regular_routers[http_method]:
            if obj.ID > router.ID:
                break
            if obj.match(url):
                router = obj
        if not router:
            router = self.match_router_in_other_http_method(url, http_method)
            if router:
                raise MethodNotAllowError
        if not router:
            raise PageNotFoundError
        return router
    
    def match_router_in_other_http_method(self, url: str, http_method: str) -> Router:
        method_list = ['GET', 'POST', 'UPDATE', 'DELETE']
        method_list.remove(http_method)
        router = None
        for method in method_list:
            router = self.routers[method].get(url, None)
            if router:
                return router
            for obj in self.regular_routers[http_method]:
                if obj.match(url):
                    return router
        return router
        
    def add(self, router: Router):
        http_method = router.http_method
        if http_method not in ['GET', 'POST', 'UPDATE', 'DELETE']:
            return
        if router.regular:
            self.regular_routers[http_method].append(router)
        else:
            if router.url in self.routers[http_method]:
                # todo warning
                pass
            self.routers[http_method][router.url] = router
    
    def group(self, middleware=None, namespace='', prefix=''):
        if middleware:
            self.group_middle.append(middleware)
        if namespace:
            self.group_namespace.append(namespace)
        if prefix:
            if not prefix.startswith('/'):
                prefix = '/' + prefix
            self.group_prefix.append(prefix)
    
    def pop_group(self, middleware=None, namespace='', prefix=''):
        if middleware:
            self.group_middle.remove(middleware)
        if namespace:
            self.group_namespace.remove(namespace)
        if prefix:
            if not prefix.startswith('/'):
                prefix = '/' + prefix
            self.group_prefix.remove(prefix)
    
    def add_group(self, url, reflect_obj_method):
        namespace = ''.join(self.group_namespace)
        prefix = ''.join(self.group_prefix)
        if namespace:
            reflect_obj_method = namespace + reflect_obj_method
        if prefix:
            url = prefix + url
        if not url.endswith('/'):
            url += '/'
        url = url.replace('//', '/')
        return url, reflect_obj_method
    
    def get(self, url, reflect_obj_method):
        url, reflect_obj_method = self.add_group(url, reflect_obj_method)
        router = Router(url, reflect_obj_method, 'GET', self.last_id)
        self.add(router)
        self.last_id += 1
        return router

    def post(self, url, reflect_obj_method):
        url, reflect_obj_method = self.add_group(url, reflect_obj_method)
        router = Router(url, reflect_obj_method, 'POST', self.last_id)
        self.add(router)
        self.last_id += 1
        return router

    def delete(self, url, reflect_obj_method):
        url, reflect_obj_method = self.add_group(url, reflect_obj_method)
        router = Router(url, reflect_obj_method, 'DELETE', self.last_id)
        self.add(router)
        self.last_id += 1
        return router

    def update(self, url, reflect_obj_method):
        url, reflect_obj_method = self.add_group(url, reflect_obj_method)
        router = Router(url, reflect_obj_method, 'UPDATE', self.last_id)
        self.add(router)
        self.last_id += 1
        return router

    def dispatch(self, request):
        router_obj = self.match_router(request.url, request.method)
        middleware = router_obj.middleware[:]
        name, method = router_obj.reflect_obj_method.split('@')
        return (Pipeline(self.app)).send(request) \
            .through(middleware) \
            .then(self.make_and_run_method(name, method, request.parameter))
    
    def make_and_run_method(self, name: str, method: str, parameter=None):
        class_name = name.split(".")[-1]
        obj = self.app.make_obj(name, class_name, parameter)
        def run_method(request):
            if hasattr(obj, method):
                if parameter:
                    return getattr(obj, method)(parameter)
                return getattr(obj, method)()
            else:
                raise Exception("Object method not found")
        return run_method
