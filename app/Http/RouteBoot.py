# -*- coding: utf-8 -*-
import routes.api as api

class RouteBoot():
    
    def boot(self):
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
