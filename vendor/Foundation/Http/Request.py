# -*- coding: utf-8 -*-


class Request():
    
    def __init__(self, env):
        """
        Create a request instance.
        @param env: dict
        """
        self.env = env
        self.method = env['REQUEST_METHOD']
        self.url = env['REQUEST_URI']
        self.parameter = {}
        if 'REQUEST_URI' in env.keys():
            self.parameter = self.parameter_init(env['REQUEST_URI'])
    
    def parameter_init(self, http_referer):
        """
        Split a url parameter to dict.
        @param http_referer: string
        @return: dict
        """
        parameter = {}
        parameter_list = http_referer.split('?')
        if len(parameter_list) > 1:
            parameter_list = parameter_list[1].split('&')
            for parameter in parameter_list:
                pairs = parameter.split('=')
                parameter[pairs[0]] = pairs[1]
        return parameter
    
    def parameters(self):
        """
        return a url parameters
        @return: dict
        """
        return self.parameter
    
    def has_parameter(self, key):
        """
        query a key in parameters
        @return: bool
        """
        return key in self.parameter
    
    def get_parameter(self, key):
        """
        get a parameter in parameters by key
        @param key: string
        @return: string
        """
        return self.parameter.get(key, "")
    
    def set_parameter(self, key, content):
        """
        get a parameter in parameters by key
        @param key: string
        @param content: string
        @return: none
        """
        self.parameter[key] = content
