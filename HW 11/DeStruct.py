import sys
import base64

s = sys.stdin.buffer.read().strip()
new_s = base64.b85decode(s)

b = bytearray(new_s)
pos = 0
arr = []
signed_arr = []

while b[pos] != 0: # заголовок
    if (b[pos] >> 7) & 1:
        arr.append(256 - b[pos])
        signed_arr.append(True)
    else:
        arr.append(b[pos])
        signed_arr.append(False)
    pos += 1
pos += 1

res_arr = []
while pos < len(b):
    for i in range(len(arr)):
        if signed_arr[i] == True:
            res_arr.append(int.from_bytes(b[pos:pos+arr[i]], byteorder='big', signed=True))
        else:
            res_arr.append(int.from_bytes(b[pos:pos+arr[i]], byteorder='big', signed=False))
        pos += arr[i]

print(sum(res_arr))   
