'''
Ввести через запятую три числа: a, b и c,
вывести решение уравнения ax²+bx+c=0.
При a≠0 это уравнение превращается в квадратное.
Решения выводить через пробел в порядке возрастания,
если решений нет, вывести 0, если их бесконечно много — -1.'''

from math import *
a, b, c = map(float, input().split(','))
if a == 0:
    if b == 0:
        if c == 0:
            print(-1)
        else:
            print(0)
    else:
        x = -c/b
        print(x)
else:
    D = b**2 - 4 * a * c
    if D < 0:
        print(0)
    else:
        x1 = (-b - sqrt(D))/(2 * a)
        x2 = (-b + sqrt(D))/(2 * a)
        if x2 > x1:
            print(x1, x2)
        elif x2 == x1:
            print(x1)
        else:
            print(x2, x1)

            
            
