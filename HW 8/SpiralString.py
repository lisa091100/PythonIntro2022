from collections import Counter
from collections import OrderedDict

def fill_matrix(matrix, arr, x0, y0, n, r):
    j = 0
    while j < len(arr)-r:
            matrix[x0][y0] = arr[j]
            j += 1
            for i in range(1, n):
                if i % 4 == 1:
                    k = 0
                    while k < i:
                        y0 += 1
                        matrix[x0][y0] = arr[j]
                        j += 1
                        k += 1
                elif i % 4 == 2:
                    k = 0
                    while k < i:
                        x0 -= 1
                        matrix[x0][y0] = arr[j]
                        j += 1
                        k += 1
                elif i % 4 == 3:
                    k = 0
                    while k < i:
                        y0 -= 1
                        matrix[x0][y0] = arr[j]
                        j += 1
                        k += 1
                elif i % 4 == 0:
                    k = 0
                    while k < i:
                        x0 += 1
                        matrix[x0][y0] = arr[j]
                        j += 1
                        k += 1
    return matrix, x0, y0

def work(arr, count):
    if len(arr) == 1:
        return arr
    else:
        n = 2
        while (n - 1)*(n + 2) <= 2 * (len(arr) - 2):
            n += 1

        S_2 = int((n - 1)*(n - 2)/2 + n)
        r = len(arr) - S_2 #Количество букв в остатке

        if r + 1 != n:
            m = n - 1
        else:
            m = n
        if ((n - 1) % 4) % 2 == 0: # n -вертикаль
            matrix = [[" "]* m for i in range(n)]
            if (n - 1) % 4 == 2:
                x0 = n - 1 - 2 * (n//4)
                y0 = 2 * (n//4)
                matrix, x, y = fill_matrix(matrix, arr, x0, y0, n, r)
                j = len(arr) - r
                while j < len(arr):
                    y -= 1
                    matrix[x][y] = arr[j]
                    j += 1
            if (n - 1) % 4 == 0:
                x0 = n - 1 - 2 * (n//4)
                y0 = 2 * (n//4)
                matrix, x, y = fill_matrix(matrix, arr, x0, y0, n, r)
                j = len(arr) - r
                while j < len(arr):
                    y += 1
                    matrix[x][y] = arr[j]
                    j += 1
        else:
            matrix = [[" "]* n for i in range(m)]
            if (n - 1) % 4 == 1:
                x0 = 2 * (m//4)
                y0 = 2 * (n//4)
                matrix, x, y = fill_matrix(matrix, arr, x0, y0, n, r)
                j = len(arr) - r
                while j < len(arr):
                    x -= 1
                    matrix[x][y] = arr[j]
                    j += 1
            if (n - 1) % 4 == 3:
                x0 = 2 * ((m+1)//4)
                y0 = 2 * (n//4)
                matrix, x, y = fill_matrix(matrix, arr, x0, y0, n, r)
                j = len(arr) - r
                while j < len(arr):
                    x += 1
                    matrix[x][y] = arr[j]
                    j += 1
        out = []
        for i in range(len(matrix)):
            out.append("".join(matrix[i]))
        return "\n".join(out)

class Spiral():
    def __init__(self, s):
        self.s = s
        res = ''.join(OrderedDict.fromkeys(self.s).keys())
        count = Counter(self.s)
        arr = []
        for i in res:
            arr += count[i]*i
        self.s = arr
    
    def __add__(self, other):
        S = self.s + other.s
        return Spiral(S)
    
    def __sub__(self, other):
        res = ''.join(OrderedDict.fromkeys(self.s).keys())
        count1 = Counter(self.s)
        count2 = Counter(other.s)
        count1.subtract(count2)
        for i in count1:
            if count1[i] < 0:
                count1[i] = 0
        arr = ""
        for i in res:
            arr += i*count1[i]
        return Spiral(arr)
    
    def __mul__(self, number):
        S = self.s * number
        return Spiral(S)
    
    def __iter__(self):
        return iter(self.s)
    
    def __repr__(self):
        res = ''.join(OrderedDict.fromkeys(self.s).keys())
        count = Counter(self.s)
        arr = ""
        for i in res:
            arr += count[i]*i
        return work(arr, count)

