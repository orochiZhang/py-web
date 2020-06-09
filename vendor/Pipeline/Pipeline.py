# -*- coding: utf-8 -*-
from functools import reduce
from vendor.Contracts.Pipeline import Pipeline as PipelineContract

class Pipeline (PipelineContract):
    # The container implementation.
    # @var \Contracts\Container
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

    # Create a new class instance.
    # @param  \Contracts\Container|null  container
    # @return void
    def __init__(self, container = None):
        self.container = container

    # Set the object being sent through the pipeline.
    # @param  mixed  $passable
    # @return self
    def send(self, passable):

        self.passable = passable
        return self

    # Set the array of pipes.
    # @param  array|mixed  $pipes
    # @return self
    def through(self, pipes, *args):
        self.pipes = pipes if type(pipes) is list else args
        return self

    # Set the method to call on the pipes.
    # @param  string  method
    # @return self
    def via(self, method):
        self.method = method
        return self

    # Run the pipeline with a final destination callback.
    # @param  \Closure  destination
    # @return mixed
    def then(self, destination):
        self.pipes.reverse()
        self.pipes.insert(0, self.prepareDestination(destination))
        pipeline = reduce(self.carry, self.pipes)
        return pipeline(self.passable)

    # Get the final piece of the Closure onion.
    # @param  \Closure  $destination
    # @return \Closure
    def prepareDestination(self, destination):
        def closure(passable):
            return destination(passable)
        return closure

    # Get a Closure that represents a slice of the application onion.
    # @return \Closure
    def carry(self, stack, pipe):
        def function1(passable):
            nonlocal pipe
            if callable(pipe):
                # If the pipe is an instance of a Closure, we will just call it directly but
                # otherwise we'll resolve the pipes out of the container and call it with
                # the appropriate method and arguments, returning the results back out.
                print(pipe)
                return pipe().handle(passable, stack)
            elif type(pipe) is str:
                name, parameters = self.parsePipeString(pipe)
                # If the pipe is a string we will parse the string and resolve the class out
                # of the dependency injection container. We can then build a callable and
                # execute the pipe function giving in the parameters that are required.
                pipe = self.getContainer().make(name)

                parameters = [passable, stack, parameters]
            else:
                # If the pipe is already an object we'll just make a callable and pass it to
                # the pipe as-is. There is no need to do any extra parsing and formatting
                # since the object we're given was already a fully instantiated object.
                parameters = [passable, stack]
            
            if hasattr(pipe, self.method):
                return getattr(pipe, self.method)(*parameters)
            else:
                return pipe(*parameters)
        
        return function1

    # Parse full pipe string to get name and parameters.
    # @param  string $pipe
    # @return array
    def parsePipeString(self, pipe: str):
        name, parameters = pipe.split(":", 2)
        
        if type(parameters) is str:
            parameters = parameters.split(",")
        
        return name, parameters

    # Get the container instance.
    # @return \Illuminate\Contracts\Container\Container
    # @throws \RuntimeException
    def getContainer(self):
        if not self.container:
            raise Exception('A container instance has not been passed to the Pipeline.')
        
        return self.container


