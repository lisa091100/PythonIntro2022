import re

def exchange(i):
    copy_i = []
    j = 0
    while j < len(i):
        if i[j] != "/":
            copy_i.append(i[j])
        else:
            copy_i.append("//")
        j += 1
    res = "".join(copy_i)
    return res

def BoldCalc(arr):
    for i in arr:
        try:
            i = re.sub(r"(?P<group>[A-Za-z_][\dA-Za-z_]*)", r"\g<group>_error", i)
            if re.findall(r"(//)|(\*\*)|([\dA-Za-z_]+\()|(\d\()|([\dA-Za-z_]+ ?= ?\d+\.\d+)", i):
                raise SyntaxError
            if "/" in i:
                new_i = exchange(i)
            else:
                new_i = i
            if "=" in new_i:
                ind = new_i.index("=")
                name = "".join(new_i[:ind].split())
                if name.isidentifier():
                    res = eval(new_i[ind + 1:])
                    exec("%s = %d" % (name, res))
                else:
                    raise AttributeError
            else:                    
                print(eval(new_i, locals()))
        except NameError:
            print("Name error")
        except AttributeError:
            print("Assignment error")
        except (SyntaxError, TypeError):
            print("Syntax error")
        except:
            print("Runtime error")
arr = []
s = str(input())
while s != "":
    if s[0] != '#':
        arr.append(s)
    s = input()
BoldCalc(arr)
