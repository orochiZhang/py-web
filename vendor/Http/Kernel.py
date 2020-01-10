# -*- coding: utf-8 -*-
from vendor.Http.Request import Request
from vendor.Http.Respone import Respone

class Kernel():
	
	def Handle(self, env):
		http_request = Request(env)
		