'''Подсчёт кратных
Написать функцию moar(a, b, n) от трёх параметров — целочисленных последовательностей a и b, и натурального числа n. 
Функция возвращает True, если в a больше чисел, кратных n, чем в b, и False в противном случае.

Примеры
Входные данные
print(moar((25,0,-115,976,100500,7),(32,5,78,98,10,9,42),5))
Результат работы
True'''

def moar(a, b, n):
    count_a = 0
    count_b = 0
    for i in range(len(a)):
        if a[i] % n == 0:
            count_a += 1
    for j in range(len(b)):
        if b[j] % n == 0:
            count_b += 1
    if count_a > count_b:
        return True
    else:
        return False
    
