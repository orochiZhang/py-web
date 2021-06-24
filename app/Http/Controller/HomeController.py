# -*- coding: utf-8 -*-
from werkzeug.wrappers import Response

class HomeController():
    
    def test(self):
        return Response("Hello, World!")
    
    def test2(self):
        return Response("Hello, homepage!")
