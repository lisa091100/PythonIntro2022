import sys
from io import BytesIO
import tarfile
import pickle

data = sys.stdin.read()
new_data = "".join(data.split())
res = BytesIO(bytes.fromhex(new_data))

count = 0
sum_data = 0
with tarfile.open(name = None, mode = "r", fileobj = res) as tar:
    for file in tar.getmembers():
        if file.isfile() == True:
            count += 1
            sum_data += file.size

print(sum_data, count)
