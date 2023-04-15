import sys
import itertools
from itertools import permutations

def code(string, code_1, code_2):
    return string.encode(code_1).decode(code_2)

def inv_code(string, code_1, code_2):
    return string.decode(code_1).encode(code_2)

#def print_res(s, i):
#    for m in range(len(s)):
#        print(code(s[m], i, 'koi8-r'))
    
list_of_acceptable_encodings = ['cp037', 'cp1006', 'cp1250', 'cp1251',
                                'cp1253', 'cp1254', 'cp1255', 'cp1256',
                                'cp1257', 'cp1258', 'cp437', 'cp720',
                                'cp737', 'cp775', 'cp850', 'cp852',
                                'cp855', 'cp864', 'cp866', 'cp869',
                                'cp874', 'cp875', 'hp_roman8', 'iso8859_10',
                                'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r',
                                'latin_1', 'mac_croatian', 'mac_greek', 'mac_iceland',
                                'mac_latin2']

#txt =str("ЪЫЩж ИЩЫЖРНЩ();\n     ЭвЭЩН: ЦЩкОЮ ЫЖРЭУЮУн ЩЗЫЖРЩЦ ТЬХЩЭУн ХУмЧЩЬЮУ.\n    НЩ ЩЮ ЭЬО 0-8-6+4/ЭЬОЦ;\n    ЪЫЩж ОЬХУ 6()6=7+6()3::\n\
#ЭвЭЩН: ЪЫУмОЦ 7.\n     ЭвЭЩН: ЭОЬд НЫТИ ЪЫЩОФЮЖ ЭЬОЦ ОЦТ ЪЫУСЩНУЮЬн?\nФЧж;")

s = sys.stdin.buffer.read().strip().decode("utf-8").strip()
#s = txt.strip()
#print(s)
def f(s):
    begin = s[0:4] # ПРОЦ
    end = s[-4:]   # КНЦ;
    if begin + end == "ПРОЦКНЦ;":
        print("".join(s))
    else:
        #s = s.split("\n")
        my_dict = {}
        for i, j in permutations(list_of_acceptable_encodings, 2): 
            try:
                my_dict[(j, i)] = code("АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЫЬЭЮЯ()[]+-*/%;.,>=<!:", "koi8-r", i).encode(j) # Проверяем какие подходят для ASCII
                
                if code(begin + end, i, 'koi8-r') == "ПРОЦКНЦ;":
                    #print_res(s, i)
                    print(code(s, i, 'koi8-r'))
                    return None
            except:
                pass
        second_my_dict = {}
        for key, val in my_dict.items():
            for i, j in permutations(list_of_acceptable_encodings, 2):
                if i != key[0]:
                    try:
                        second_my_dict[((j, i), key)] = inv_code(val, i, j)
                        if code(code(begin + end, i, key[0]), key[1], 'koi8-r') == "ПРОЦКНЦ;":
                            #for m in range(len(s)):
                            #    print(code(code(s[m], i, key[0]), key[1],'koi8-r'))
                            print(code(code(s, i, key[0]), key[1],'koi8-r'))
                            return None
                    except:
                        pass
        for key, val in second_my_dict.items():
            for i, j in permutations(list_of_acceptable_encodings, 2):
                if i != key[0][0]:
                    try:
                        tmp = inv_code(val, i, j)
                        #print(code(code(code(begin + end, i, key[0][0]), key[0][1], key[1][0]), key[1][1], 'koi8-r'))
                        if code(code(code(begin + end, i, key[0][0]), key[0][1], key[1][0]), key[1][1], 'koi8-r') == "ПРОЦКНЦ;":
                            #for m in range(len(s)):
                            #    s[m] = code(code(code(s[m], i, key[0][0]), key[0][1], key[1][0]), key[1][1], 'koi8-r')
                            #print("\n".join(s))
                            #print('*')
                            s = code(code(code(s, i, key[0][0]), key[0][1], key[1][0]), key[1][1], 'koi8-r')
                            print(s)
                            return None   
                    except:
                        pass

a = f(s)
