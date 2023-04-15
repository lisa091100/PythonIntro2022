from decimal import Decimal
from math import *
import decimal

def bisect(f, a, b, num):
    a = Decimal(a)
    b = Decimal(b)
    x = (a+b) / Decimal(str(2.0))
    check = f(x)
    const = check + 1
    while check != const and abs(check) > Decimal(10**(-num-1)):
        if f(a)* f(x) > 0:
            a = Decimal(x)
        else:
            b = Decimal(x)
        x = (a+b) / Decimal(str(2.0))
        const = check
        check = f(x)
    return x

str_f = input()
num = int(input())
if str_f == "x":
    print("0." + "0" * num)
else:
    decimal.getcontext().prec=num+2
    f = lambda x: Decimal(eval(str_f))
    print(round(bisect(f, -1.5, 1.5, num), num))

