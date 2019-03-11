# coding=utf-8

import json
from budd.util import wrapper_hook


@wrapper_hook(__name__)
def value_processor(v):
    try:
        v = json.loads(v)
        return v
    except ValueError as e:
        raise e
