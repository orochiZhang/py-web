# -*- coding: utf-8 -*-
from vendor.Facade.Route import Route

import routes.api as api


class RouteBoot():
    namespace = 'app.Http.Controller.'
    
    def boot(self):
        Route().group(namespace=self.namespace)
        self.map()
    
    def map(self):
        self.init_api_routes()
        self.init_web_routes()
        self.init_admin_routes()
    
    def init_api_routes(self):
        api.init()
    
    def init_web_routes(self):
        pass
    
    def init_admin_routes(self):
        pass
