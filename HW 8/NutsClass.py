class Nuts:
    def __init__(self, *params):
        pass
    def __getitem__(self, index):
        return index
    def __iter__(self):
        s = "Nuts"
        res = iter([i for i in s])
        return res
    def __getattr__(self, name):
        return name
    def __setattr__(self, name, value):
        pass
    def __setitem__(self, key, value):
        pass
    def __str__(self):
        return "Nuts"
    def __delattr__(self, name):
        pass
    def __delitem__(self, key):
        pass
    
