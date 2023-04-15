from collections import defaultdict

def statcounter():
    my_dict = {}
    res = yield my_dict

    def send(key_function):
        def fun(*args, **kwargs):
            if key_function not in my_dict.keys():
                my_dict[key_function] = 1
            else:
                my_dict[key_function] += 1
            return key_function(*args, **kwargs)
        return fun
    while True:
        my_dict[res] = 0
        res = yield send(res)

