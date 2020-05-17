# -*- coding: utf-8 -*-

from werkzeug.wrappers import Request, Response
from bootstrap import app
from vendor.Facade.Route import Route
from vendor.Router.Route import Route as RouteSingleton

import vendor.Contracts.Kernel
import vendor.Contracts.Request

@Request.application
def application(request):
    _app = app.get_application()
    _app.singleton('Route', RouteSingleton(_app))
    Route.get('/home', 'HomeController@test')
    kernel = _app.make(vendor.Contracts.Kernel.Kernel)
    http_request = _app.make(vendor.Contracts.Request.Request, [request.environ])
    response = kernel.handle(http_request)
    return response
    # return Response("Hello, World!")

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    run_simple("localhost", 5000, application)