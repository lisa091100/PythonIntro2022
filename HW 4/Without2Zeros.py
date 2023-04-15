'''
Без двух нулей
Написать функцию No_2Zero(N, K), которая вычисляет количество N-значных чисел в системе
 счисления с основанием K, таких что их запись не содержит двух подряд идущих нулей. Лидирующие 
нули не допускаются. Для EJudge N⩽33.

Примеры

Входные данные
print(No_2Zero(6, 3))

Результат работы
328
'''

def No_2Zero(N, K):
    without0 = K - 1
    with0 = 0
    for i in range(N-1):
        next_without0 = (without0 + with0) *(K-1)
        next_with0 = without0
        without0 = next_without0
        with0 = next_with0
    return without0 + with0
