from decimal import Decimal
from math import *
import decimal

def PiGen():
    decimal.getcontext().prec = 10000
    a = Decimal(426880)*Decimal(10005).sqrt()
    S = Decimal(13591409)
    yield a/S
    for k in range(1, 10001):
        res = Decimal(Decimal(545140134)*k)+Decimal(13591409)
        temp_k = 1
        for i in range(1, k + 1):
            temp_k *= Decimal(i)
        temp_3k = Decimal(temp_k)
        temp_k = Decimal(Decimal(temp_k)**3)
        for i in range(k + 1, 3*k+1):
            temp_3k *= Decimal(i)
        temp_6k = Decimal(temp_3k)
        for i in range(3*k + 1, 6*k+1):
            temp_6k *= Decimal(i)
        S += Decimal(Decimal(temp_6k)*Decimal(res))/Decimal(temp_3k)/Decimal(temp_k)/Decimal(Decimal(-262537412640768000)**k)
        yield a/S
    

