import numbers
import types
import inspect
import typing
from typing import get_origin

def function(f):
    def new_f(*args, **kwargs):
        res = ()
        params = inspect.signature(f).parameters
        for i, j in params.items():
            if i == 'self':
                continue
            if j.default is j.empty:
                if isinstance(params[i].annotation, types.GenericAlias):
                    res += (params[i].annotation.__origin__(),)
                else:
                    try:
                        res += (params[i].annotation(),)
                    except:
                        res += (None,)
        if f.__defaults__ is None:
            f.__defaults__ = ()
        f.__defaults__ = res + f.__defaults__
        return f(*args, **kwargs)
    return new_f


class init(type):
    @staticmethod
    def __new__(metacls, name, parents, attrs, **kwds):
        my_dict = vars()['attrs']
        for key, val in my_dict.items():
            if type(val) == types.FunctionType:
                attrs[key] = function(val)
        return super().__new__(metacls, name, parents, attrs)
