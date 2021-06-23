# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Request(ABC):
    
    @abstractmethod
    def parameters(self):
        """
        return a url parameters
        @return: dict
        """
        pass

    @abstractmethod
    def has_parameter(self, key):
        """
        query a key in parameters
        @return: bool
        """
        pass

    @abstractmethod
    def get_parameter(self, key):
        """
        get a parameter in parameters by key
        @param key: string
        @return: string
        """
        pass

    @abstractmethod
    def set_parameter(self, key, content):
        """
        get a parameter in parameters by key
        @param key: string
        @param content: string
        @return: none
        """
        pass