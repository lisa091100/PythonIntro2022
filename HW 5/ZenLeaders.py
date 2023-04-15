def input_str(s):
    name, surname, *team_s, time = map(str, s.split(' '))
    time_arr = time.split(':')
    time_arr = [int(i) for i in time_arr]
    team = ' '.join(team_s)
    return [name, surname, team, time_arr]

def modern_arr(i, j, arr):
    while arr[i][3] == arr[j][3]:
       j += 1
       if j == len(arr):
           break
    arr[i:j] = sorted(arr[i:j], key = lambda x:(x[1], x[0], x[2]))
    return j

def print_res(new_arr):
    len_new_arr = len(new_arr)
    for i in range(len_new_arr):
        new_arr[i][3] = [str(i) for i in new_arr[i][3]]
        new_arr[i][3] = ":".join(new_arr[i][3])
        print(new_arr[i][0].ljust(max_len_name, " "), new_arr[i][1].ljust(max_len_surname, " "), new_arr[i][2].ljust(max_len_team, " "), new_arr[i][3])
    
exit_flag = False
arr = []
s1 = input()
count = 1
s2 = input()
if not s2:
    print(s1)
else:
    arr.append(input_str(s1))
    count += 1
    arr.append(input_str(s2))
    while True:
        s = input()
        if not s:
            if (count == 2):
                arr.sort(key = lambda x:(x[3][0], x[3][1], x[3][2]))
                j1 = modern_arr(0, 0, arr)
                arr = arr[:j1+1]
                max_len_name = max(map(lambda x: len(x[0]), arr))
                max_len_surname = max(map(lambda x: len(x[1]), arr))
                max_len_team = max(map(lambda x: len(x[2]), arr))
                print_res(arr)
            exit_flag = True
            break
        count += 1
        arr.append(input_str(s))
if exit_flag == True and count > 2:
    arr.sort(key = lambda x:(x[3][0], x[3][1], x[3][2]))
    j1 = modern_arr(0, 0, arr)
    len_arr = len(arr)
    if j1 != len_arr:
        j2 = modern_arr(j1, j1, arr)
        if j2 != len_arr:
            j3 = modern_arr(j2, j2, arr)
            new_arr = arr[:j3]
        else:
            new_arr = arr[:j2]
    else:
        new_arr = arr[:j1]
    max_len_name = max(map(lambda x: len(x[0]), new_arr))
    max_len_surname = max(map(lambda x: len(x[1]), new_arr))
    max_len_team = max(map(lambda x: len(x[2]), new_arr))
    print_res(new_arr)

    
