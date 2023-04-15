d_name = {}
d_n = {}
input_str = input()
while input_str != "":
    arr = input_str.split(" / ")
    if arr[0].isdigit():
        num =  int(arr[0])
        if not d_n.get(num, []):
            d_n[num] = []
            d_n[num].append(arr[1])
        else:
            d_n[num].append(arr[1])
    else:
        if not d_name.get(arr[0], []):
            d_name[arr[0]] = []
            d_name[arr[0]].append(int(arr[1]))
        else:
            d_name[arr[0]].append(int(arr[1]))
    input_str = input()
for i in d_n.keys():
    temp = d_n[i]
    d_n[i] = list(set(temp))
str_ = []
for i in d_name.keys():
    str_.append(i)
max_len = []
for i in d_name.keys():
    l = 0
    temp_ = []
    for j in range(len(d_name[i])):
        temp_+= d_n[d_name[i][j]]
    new_temp = list(set(temp_))
    max_len.append(len(new_temp))  
count = max(max_len)
index = [i for i in range(len(max_len)) if count == max_len[i]]
answ = []
for i in index:
    answ.append(str_[i])
answ.sort()
for i in answ:
    print(i)
