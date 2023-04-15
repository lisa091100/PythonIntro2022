'''
Ящик с точками
Вводить вещественные числа x, y и z по три в строке через запятую,
считая их координатами точек (не менее одной тройки). Конец ввода —
пустая строка. Вывести минимальный объём параллелепипеда со сторонами,
параллельными осям координат, содержащего все точки.
'''
x, y, z = map(float, input().split(','))
min_x = x
max_x = x
min_y = y
max_y = y
min_z = z
max_z = z
while True:
    str = input()
    if not str:
        break
    x, y, z = map(float, str.split(','))
    if max_x < x:
        max_x = x
    elif x < min_x:
        min_x = x
    if max_y < y:
        max_y = y
    elif y < min_y:
        min_y = y
    if max_z < z:
        max_z = z
    elif z < min_z:
        min_z = z
V = (max_x - min_x)*(max_y - min_y)*(max_z - min_z)
print(V)
