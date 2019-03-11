# coding=utf-8
from __future__ import unicode_literals
import os
import sys
import warnings
from types import ModuleType


class Module(ModuleType):
    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)

    def __getitem__(self, item):
        return getattr(self, item)

    def __setitem__(self, key, value):
        setattr(self, key, value)


class ImportHooker(object):
    """
    importer hooker
    :param warpper: 前缀， 如honeypot.raw, honeypot.json
    :param value_processor: 数据处理方法
    """

    def __init__(self, wrapper, value_processor):
        self.wrapper = wrapper
        self.value_processor = value_processor

    def __repr__(self):
        return "import_hooker:{}:{}:{}".format(
            self.__class__.__module__,
            self.__class__.__name__, self.wrapper)

    def __eq__(self, other):
        return (self.__class__.__module__ == other.__class__.__module__) and \
               (self.__class__.__name__ == other.__class__.__name__) and \
               (self.wrapper == other.wrapper)

    def install(self):
        if self not in sys.meta_path:
            sys.meta_path.append(self)

    def find_module(self, full_name, path=None):
        if full_name.startswith(self.wrapper):
            return self

    def load_module(self, full_name):
        """
        full_name: eg. honeypot.json.mar
        wrapper: eg. honeypot.json
        """
        if full_name in sys.modules:
            return sys.modules[full_name]
        m = Module(full_name)
        try:
            prefix_name = full_name[len(self.wrapper) + 1:]
        except IndexError:
            warnings.warn("you shoud use as %s.foo" % full_name, SyntaxWarning)
            prefix_name = "___"
        for k, v in self.get_env(prefix_name):
            setattr(m, k, v)
        sys.modules[full_name] = m
        return m

    def get_env(self, prefix_name):
        prefix_name = prefix_name.upper() + "_"
        for key, value in os.environ.items():
            if key.startswith(prefix_name):
                key = key[len(prefix_name):]
                value = self.value_processor(value)
                yield key, value
