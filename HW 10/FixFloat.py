def fix(n):
    def new_res(new_fun):
        def fun(*args, **kwargs):
            def round_function(arg):
                if type(arg) == float:
                    return round(arg, n)
                else:
                    return arg
            new_args = [round_function(i) for i in args]
            for key, val in kwargs.items():
                kwargs[key] = round_function(val)
            return round_function(new_fun(*new_args, **kwargs))
        return fun
    return new_res


