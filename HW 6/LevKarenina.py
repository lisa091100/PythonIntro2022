from collections import Counter
import re
import sys

def print_answer(arr):
    if len(arr) == 0:
        print("... 0", end = "")
    else:
        count = Counter(arr).most_common()
        for key, val in count:
            print(key, val, end = "")
            break
p, b, g, e = input()
s = input()
text = []
while s != "":
    text.append(s)
    s = input()
text = " ".join(text)
text = text.split()
first_arr = []
last_arr = []
for i in range(1, len(text)):
    if b in text[i] and text[i-1][-1] == p:
        first_arr.append(text[i])
    if text[i][0] == g and text[i][-1] == e:
        last_arr.append(text[i])
print_answer(first_arr)
print(" - ", end = "")
print_answer(last_arr)

