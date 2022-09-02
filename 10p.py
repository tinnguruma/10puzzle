import math
import itertools

n1 = input("1>>")
n2 = input("2>>")
n3 = input("3>>")
n4 = input("4>>")
st = int(input("START?>>"))
en = int(input("END?>>"))

ALL_list_1 = [n1,str(math.factorial(int(n1))),str(math.sqrt(int(n1)))]
ALL_list_2 = [n2,str(math.factorial(int(n2))),str(math.sqrt(int(n2)))]
ALL_list_3 = [n3,str(math.factorial(int(n3))),str(math.sqrt(int(n3)))]
ALL_list_4 = [n4,str(math.factorial(int(n4))),str(math.sqrt(int(n4)))]

symbol_list = ["-","+","*","/"]
parentheses_list = [["", "", "", "", "", ""],["(", "", ")", "", "", ""],["(", "", "", "", ")", ""],["", "(", "", "", ")", ""],["", "(", "", "", "", ")"],["", "", "", "(", "", ")"],["math.sqrt(", "", ")", "", "", ""],["math.sqrt(", "", "", "", ")", ""],["", "math.sqrt(", "", "", ")", ""],["", "math.sqrt(", "", "", "", ")"],["", "", "", "math.sqrt(", "", ")"],["math.factorial(", "", ")", "", "", ""],["math.factorial(", "", "", "", ")", ""],["", "math.factorial(", "", "", ")", ""],["", "math.factorial(", "", "", "", ")"],["", "", "", "math.factorial(", "", ")"]]
for l in range(st,en):
    for n in ALL_list_1:
        for m in ALL_list_2:
            for o in ALL_list_3:
                for p in ALL_list_4:
                    symbol_pattern = itertools.combinations_with_replacement(symbol_list, 3)
                    for q in symbol_pattern:
                        for r in parentheses_list:          
                            txt = str(r[0]) + n + q[0] + str(r[1]) + m + str(r[2]) + q[1] + str(r[3]) + o + str(r[4]) + q[2] + p + str(r[5])
                            try:              
                                if (eval(txt)==l):
                                    if("math.sqrt" in txt):
                                        txt = txt.replace("math.sqrt","√")
                                    if("math.factorial" in txt):
                                        txt = txt.replace("math.factorial","")
                                        txt = txt.replace(")",")!")
                                    print(l,txt)
                                    break
                            except:
                                pass
                        else:
                            continue
                        break
                    else:
                        continue
                    break
                else:
                    continue
                break
            else:
                continue
            break
        else:
            continue
        break
    else:
        print(str(l) + "NO!")