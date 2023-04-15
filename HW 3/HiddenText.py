'''Скрытое послание
Ввести две строки и проверить, содержится ли вторая в первой,
с учётом того, что символы второй строки могут находиться в первой
на некотором равном расстоянии друг от друга. Вывести YES или NO.

Примеры
Входные данные
q-We-Rt-Yu-Iweozzz
WRYI
Результат работы
YES'''

def all_index(string, element):
    return [i for i in range(len(string)) if string[i] == element]

print_flag = False
exitFlag = False
str1 = input()
str2 = input()
if (str2[0] in str1) == False:
    print_flag = True
    print("NO")
elif len(str2) == 1:
    print_flag = True
    if str2 in str1:
        print("YES")
    else:
        print("NO")
else:
    arr_0 = all_index(str1, str2[0])
    arr_1 = all_index(str1, str2[1])
    for i in range(len(arr_0)):
        for j in range(len(arr_1)):
            difference = arr_1[j]-arr_0[i]
            stop = arr_0[i] + len(str2)*difference
            if str1[arr_0[i]:stop:difference] == str2:
                print("YES")
                exitFlag = True
                break
        if (exitFlag):
            break
if exitFlag == False and print_flag == False:
    print("NO")
