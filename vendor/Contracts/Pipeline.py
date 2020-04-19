# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Closure():
    pass

class Pipeline(ABC):
    # Set the traveler object being sent on the pipeline.
    # @param  mixed  $traveler
    # @return self
    #
    @abstractmethod
    def send(self, traveler):
        pass


    # Set the stops of the pipeline.
    # @param  dynamic|array  $stops
    # @return self
    #
    @abstractmethod
    def through(self, stops):
        pass

    # Set the method to call on the stops.
    # @param  string  $method
    # @return $this
    @abstractmethod
    def via(self, method):
        pass


    # Run the pipeline with a final destination callback.
    # @param  Closure  $destination
    # @return mixed
    #
    @abstractmethod
    def then(self, destination: Closure):
        pass
