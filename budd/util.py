# coding=utf-8

from budd.hook import ImportHooker


def wrapper_hook(wrpper_name):
    def wrapper(func):
        importer = ImportHooker(wrpper_name, func)
        importer.install()
        return func
    return wrapper