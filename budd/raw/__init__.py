# coding=utf-8

from budd.util import wrapper_hook


@wrapper_hook(__name__)
def value_processor(v):
    return v
