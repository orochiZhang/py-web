# -*- coding: utf-8 -*-
from vendor.Facade.Route import Route

import routes.api as api

class RouteBoot():
    namespace = 'app.Http.Controller.'
    
    def boot(self):
        Route().group(namespace=self.namespace)
        self.map()
    
    def map(self):
        self.mapApiRoutes()
        self.mapWebRoutes()
        self.mapAdminRoutes()
    
    def mapApiRoutes(self):
        api.init()
    
    def mapWebRoutes(self):
        pass
    
    def mapAdminRoutes(self):
        pass
