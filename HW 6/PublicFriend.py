d = {}
input_str = input()
while input_str != "0, 0":
    arr = input_str.split(",")
    arr = [int(i) for i in arr]
    if not d.get(arr[0], []):
        d[arr[0]] = []
        d[arr[0]].append(arr[1])
    else:
        d[arr[0]].append(arr[1])
    if not d.get(arr[1], []):
        d[arr[1]] = []
        d[arr[1]].append(arr[0])
    else:
        d[arr[1]].append(arr[0])
    input_str = input()
for i in d.keys():
    temp = d[i]
    d[i] = list(set(temp))
k = []
for i in d.keys():
    if len(d[i]) == len(d.keys()) - 1:
        k.append(i)
k.sort()
print(*k)
