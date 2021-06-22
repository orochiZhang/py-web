# -*- coding: utf-8 -*-
from werkzeug.wrappers import Request
from bootstrap import app

import vendor.Contracts.Kernel
import vendor.Contracts.Request

@Request.application
def application(request):
    _app = app.get_application()
    kernel = _app.make(vendor.Contracts.Kernel.Kernel)
    http_request = _app.make(vendor.Contracts.Request.Request, [request.environ])
    response = kernel.handle(http_request)
    print("response>>>", response)
    return response

if __name__ == "__main__":
    from werkzeug.serving import run_simple
    app.boot()
    run_simple("localhost", 5000, application)
