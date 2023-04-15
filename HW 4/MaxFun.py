'''Функция побольше
Написать функцию maxfun(), которая принимает переменное число параметров — числовую
 последовательность S, функцию F1 и, возможно, ещё несколько функций F2 … Fn. Возвращает
 она ту из функций Fi, сумма значений которой на всех элементах S наибольшая. Если таких
 функций больше одной, возвращается Fi с наибольшим i.

Примеры

Входные данные
from math import *
print(maxfun(range(-2,10), sin, cos, exp)(1))

Результат работы
2.718281828459045
'''

def maxfun(S, F1, *F2):
    F1_list = [F1(i) for i in S]
    res_max_element = max(F1_list)
    res = F1
    for f in F2:
        f_list = [f(i) for i in S]
        res_f_max = max(f_list)
        if res_f_max >= res_max_element:
            res_max_element = res_f_max
            res = f
    return res
