# -*- coding: utf-8 -*-
from vendor.Foundation.Http.Middleware.TrimStrings import TrimStrings as BaseTrimStrings

class TrimStrings(BaseTrimStrings):
    except_key = [
        'password',
        'password_confirmation',
    ]
