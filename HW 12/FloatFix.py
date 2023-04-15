import numbers
import types

def function(f, ndigits):
    def new_f(*args, **kwargs):
        if isinstance(f(*args, **kwargs), numbers.Real):
            res = round(f(*args, **kwargs), ndigits)
            return res
        else:
            return f(*args, **kwargs)
    return new_f

class fixed(type):
    @staticmethod
    def __new__(metacls, name, parents, attrs, ndigits=3, **kwds):
        my_dict = vars()['attrs']
        for key, val in my_dict.items():
            if type(val) == types.FunctionType:
                attrs[key] = function(val, ndigits)
        return super().__new__(metacls, name, parents, attrs)
