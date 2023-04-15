'''Чудо-конвейер
Ввести последовательность объектов Python (только кортежей или целых чисел), и сымитировать работу Чудо-Конвейера. Если объект — кортеж, это означает, что на вход конвейеру подаются поочерёдно все объекты из этого кортежа. Если объект — натуральное число N, это означает, что с выхода конвейера надо снять поочерёдно N объектов, объединить их в кортеж и вывести. Если с конвейера нельзя снять N объектов, или в последовательности нет больше команд, Чудо-Конвейер немедленно останавливается.

Примеры
Входные данные
("QWE",1.1,234),2,(None,7),0,2,(7,7,7),2,(12,),(),3,(5,6),3,100500
Результат работы
('QWE', 1.1)
()
(234, None)
(7, 7)
(7, 7, 12)
'''
arr = []
arguments = eval(input())
for element in arguments:
    if type(element) is tuple:
        for j in element:
            arr.append(j)
    elif type(element) is int:
        if element == 0:
            print(tuple())
        elif element > len(arr):
            break
        else:
            reversed_arr = list(reversed(arr))
            print_arr = []
            for k in range(element):
                print_arr.append(arr[k])
                reversed_arr.pop()
            arr = list(reversed(reversed_arr))
            print(tuple(print_arr))
