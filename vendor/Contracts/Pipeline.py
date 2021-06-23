# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Closure():
    pass

class Pipeline(ABC):

    @abstractmethod
    def send(self, traveler):
        """
        Set the traveler object being sent on the pipeline.
        @param traveler: mixed
        @return: self
        """
        pass

    @abstractmethod
    def through(self, stops):
        """
        Set the stops of the pipeline.
        @param stops: dynamic|array
        @return: self
        """
        pass

    @abstractmethod
    def via(self, method):
        """
        Set the method to call on the stops.
        @param method: string
        @return: self
        """
        pass

    @abstractmethod
    def then(self, destination: Closure):
        """
        Run the pipeline with a final destination callback.
        @param destination: Closure
        @return: mixed
        """
        pass
