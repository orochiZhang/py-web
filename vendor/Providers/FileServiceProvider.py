# -*- coding: utf-8 -*-
from .ServiceProvider import ServiceProvider
from vendor.File.FileSystem import FileSystemA


# 简单的File服务提供者
class FileServiceProvider(ServiceProvider):

    def register(self):
        def get_file_system():
            return FileSystemA()

        self.app.register('files', get_file_system)
