from random import random
from math import *

def randsquare(A, B):
    a = sqrt(((B[0] - A[0])**2 + (B[1] - A[1])**2)/2)
    O = ((A[0] + B[0])/2, (A[1] + B[1])/2)
    OC = (-(B[1] - A[1]) / 2, (B[0] - A[0]) / 2)
    C = (O[0] + OC[0], O[1] + OC[1])
    D = (O[0] - OC[0], O[1] - OC[1])
    AD = (D[0] - A[0], D[1] - A[1])
    AC = (C[0] - A[0], C[1] - A[1])
    x = random()
    y = random()
    x_res = AD[0]*x + AC[0]*y + A[0]
    y_res = AD[1]*x + AC[1]*y + A[1]
    return (x_res, y_res)

