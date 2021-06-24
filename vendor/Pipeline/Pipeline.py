# -*- coding: utf-8 -*-
from functools import reduce
from inspect import isfunction, ismethod
from vendor.Contracts.Pipeline import Pipeline as PipelineContract

class Pipeline(PipelineContract):
    # The container implementation.
    # @var Contracts.Container
    container = None

    # The object being passed through the pipeline.
    # @var mixed
    passable = None

    # The array of class pipes.
    # @var list
    pipes = []

    # The method to call on each pipe.
    # @var string
    method = 'handle'

    def __init__(self, container=None):
        """
        Create a new class instance.
        @param container: Contracts.Container|null
        """
        self.container = container

    def send(self, passable):
        """
        Set the object being sent through the pipeline.
        @param passable: mixed
        @return: self
        """
        self.passable = passable
        return self

    def through(self, pipes, *args):
        """
        Set the array of pipes.
        @param pipes: array|mixed
        @param args: mixed
        @return: self
        """
        self.pipes = pipes if type(pipes) is list else args
        return self

    def via(self, method):
        """
        Set the method to call on the pipes.
        @param method: string
        @return: self
        """
        self.method = method
        return self

    def then(self, destination):
        """
        Run the pipeline with a final destination callback.
        @param destination: Closure
        @return: mixed
        """
        self.pipes.reverse()
        self.pipes.insert(0, destination)
        pipeline = reduce(self.carry, self.pipes)
        return pipeline(self.passable)

    def prepare_destination(self, destination):
        """
        Get the final piece of the Closure onion.
        @param destination: Closure
        @return: Closure
        """
        def closure(passable):
            return destination(passable)
        return closure

    def carry(self, stack: list, pipe):
        """
        Get a Closure that represents a slice of the application onion.
        @param stack: list
        @param pipe:
        @return: Closure
        """
        def create_closure(passable):
            nonlocal pipe
            nonlocal self
            if ismethod(pipe) or isfunction(pipe):
                # If the pipe is a function type, we will just call it directly but
                # otherwise we'll resolve the pipes out of the container and call it with
                # the appropriate method and arguments, returning the results back out.
                return pipe(passable, stack)
            elif pipe is type:
                # If the pipe is a class type, we will just call it directly and
                # create an instance of the class.
                pipe = pipe()
                parameters = [passable, stack]
            elif type(pipe) is str:
                name, parameters = self.parse_pipe_string(pipe)
                # If the pipe is a string we will parse the string and resolve the class out
                # of the dependency injection container. We can then build a callable and
                # execute the pipe function giving in the parameters that are required.
                pipe = self.get_container().make(name)

                parameters = [passable, stack, parameters]
            else:
                # If the pipe is already an instance of class, we'll just make a callable and pass it to
                # the pipe as-is. There is no need to do any extra parsing and formatting
                # since the object we're given was already a fully instantiated object.
                parameters = [passable, stack]
            
            if hasattr(pipe, self.method):
                return getattr(pipe, self.method)(pipe, *parameters)
            else:
                return pipe(*parameters)
        
        return create_closure
    
    def parse_pipe_string(self, pipe: str):
        """
        Parse full pipe string to get name and parameters.
        @param pipe: string
        @return: array
        """
        name, parameters = pipe.split(":", 2)
        if type(parameters) is str:
            parameters = parameters.split(",")
        return name, parameters

    def get_container(self):
        """
        Get the container instance.
        @return: Contracts.Container
        @throws Exception
        """
        if not self.container:
            raise Exception('A container instance has not been passed to the Pipeline.')
        return self.container
