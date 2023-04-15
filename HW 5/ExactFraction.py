from fractions import Fraction
import re
s = str(input())
arr = re.findall(r'\d*\.\d+|\d+|\+|\-|\(|\*|\/|\)|\%', s)
symb = ["+", "-", "/", "*", "(", ")", "%"]
for i in range(len(arr)):
    count = 0
    for j in symb:
        if arr[i] != j:
            count += 1
    if count == len(symb):
        arr[i] = Fraction(str(float(arr[i]))).__repr__() 
res = ''.join(arr)
print(eval(res))
