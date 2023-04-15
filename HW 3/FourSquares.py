'''
Известно, что любое натуральное число можно представить в виде
суммы не более чем четырех квадратов неотрицательных целых чисел
(теорема Лагранжа). Ввести натуральное N⩽100000 и найти для него такие
целые неотрицательные x,y,z и t, чтобы x²+y²+z²+t²=N. Вывести все такие
четвёрки в следующем формате: x,y,z и t — через пробел, и упорядочены по
убыванию, а сами четвёрки — лексикографически по возрастанию (без повторений).

Примеры
Входные данные
100
Результат работы
5 5 5 5
7 5 5 1
7 7 1 1
8 4 4 2
8 6 0 0
9 3 3 1
10 0 0 0
'''
from math import *
N = int(input())
for x in range(round(N**(1/4)), int(sqrt(N)) + 1):
    for y in range(int((sqrt(N-x**2))/3), min(x, int((sqrt(N-x**2))))+1):
        for z in range(int(sqrt(N-x**2 - y**2)/2), min(y, int((sqrt(N - x**2 - y**2))))+1):
            if N - x**2 - y**2 - z**2 <= z**2 and N - x**2 - y**2 - z**2 >= 0:
                t = int(sqrt(N - x**2 - y**2 - z**2))
                if x**2 + y**2 + z**2+ t**2 == N:
                    print(x, y, z, t)