'''
Длиннейшая подпоследовательность
Вводить по одному непустую последовательность целых чисел, не равных нулю.
Ноль означает конец в вода и не учитывается. Вывести наибольшую длину
неубывающей подпоследовательности подряд идущих чисел исходной
последовательности. Хранить введённую последовательность или её невырожденную
подпоследоватиельность запрещается.'''

num = int(input())
old_num = num
count = 1
max_count = 0
while num != 0:
    num = int(input())
    if num >= old_num:
        count += 1
    else:
        if(max_count < count):
            max_count = count
        count = 1
    old_num = num
print(max_count)
