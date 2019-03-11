# coding=utf-8

import json
from json.decoder import JSONDecodeError

from budd.util import wrapper_hook


@wrapper_hook(__name__)
def value_processor(v):
    try:
        v = json.loads(v)
        return v
    except JSONDecodeError as e:
        raise e
