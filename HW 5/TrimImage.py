count = 0
new_arr = []
output = []
while True:
    str_in = input()
    if not str_in:
        break
    count += 1
    arr_str = str_in.split(" ")
    arr_str[:len(arr_str)-1] = [int(arr_str[i]) for i in range(len(arr_str)-1)]
    if arr_str[2] == 0 or arr_str[3] == 0:
        continue
    if arr_str[2] < 0:
        arr_str[0] += arr_str[2]
        arr_str[2] *= -1
    if arr_str[3] < 0:
        arr_str[1] += arr_str[3]
        arr_str[3] *= -1
    if count == 1:
        min_x = arr_str[0]
        min_y = arr_str[1]
        max_x = arr_str[0] + arr_str[2]
        max_y = arr_str[1] + arr_str[3]
    else:
        if arr_str[0] < min_x:
            min_x = arr_str[0]
        if arr_str[1] < min_y:
            min_y = arr_str[1]
        if max_x < arr_str[0] + arr_str[2]:
            max_x = arr_str[0] + arr_str[2]
        if max_y < arr_str[1] + arr_str[3]:
            max_y = arr_str[1] + arr_str[3]
    arr_str[2] = arr_str[0] + arr_str[2]
    arr_str[3] = arr_str[1] + arr_str[3]
    new_arr.append(arr_str)
output = [["."]*(max_x - min_x) for i in range(max_y-min_y)]
for i in range(len(new_arr)):
    for j in range(new_arr[i][1] - min_y, new_arr[i][3] - min_y):
        for k in range(new_arr[i][0] - min_x, new_arr[i][2] - min_x):
            output[j][k] = new_arr[i][4]
for i in output:
    print(''.join(i))
