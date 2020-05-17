# -*- coding: utf-8 -*-
from werkzeug.wrappers import Response

class HomeController():
    
    def test(self):
        return Response("Hello, World!")
