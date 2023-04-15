def sloter(fields, default):
    class slo:
        __slots__ = [str(i) for i in fields]
        
        def __init__(self):
            for name in self.__slots__:
                setattr(self, name, default)

        def __delattr__(self, attr):
            return setattr(self, attr, default)
        
        def __iter__(self):
            arr = []
            for name in self.__slots__:
                arr.append(getattr(self, name))
            return iter(arr)
    return slo
