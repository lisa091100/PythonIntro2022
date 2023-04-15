class Pushpull:
    num = 0

    def __init__(self, step = 0):
        Pushpull.num = step
        
    def push(self, step = 1):
        Pushpull.num += step
        
    def pull(self, step = 1):
        Pushpull.num -= step
        
    def __iter__(self):
        if Pushpull.num >= 0:
            res = iter([i for i in range(0, Pushpull.num)])
        else:
            res = iter([i for i in range(0, Pushpull.num, -1)])
        return res
    
    def __str__(self):
        if Pushpull.num > 0:
            return f">{Pushpull.num}>"
        elif Pushpull.num == 0:
            return "<0>"
        else:
            return f"<{-Pushpull.num}<"
        
