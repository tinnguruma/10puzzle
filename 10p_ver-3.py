mport math
import itertools
import re
from traceback import format_exc

n1 = input("1>>")
n2 = input("2>>")
n3 = input("3>>")
n4 = input("4>>")

ALL_list_1 = [n1, str("r" + n1), str("k" + n1), str("kr" + n1), str("rk" + n1)]
ALL_list_2 = [n2, str("r" + n2), str("k" + n2), str("kr" + n2), str("rk" + n2)]
ALL_list_3 = [n3, str("r" + n3), str("k" + n3), str("kr" + n3), str("rk" + n3)]
ALL_list_4 = [n4, str("r" + n4), str("k" + n4), str("kr" + n4), str("rk" + n4)]

symbol_list = ["-", "+", "*", "/"]
parentheses_list = [["", "", "", "", "", ""], ["(", "", ")", "", "", ""], ["(", "", "", "", ")", ""], ["", "(", "", "", ")", ""], 
                    ["", "(", "", "", "", ")"], ["", "", "", "(", "", ")"], 
                    ["math.sqrt(", "", ")", "", "", ""], ["math.sqrt(", "", "", "", ")", ""], ["", "math.sqrt(", "", "", ")", ""], ["", "math.sqrt(", "", "", "", ")"], 
                    ["", "", "", "math.sqrt(", "", ")"], ["math.factorial(", "", ")", "", "", ""], ["math.factorial(", "", "", "", ")", ""], ["", "math.factorial(", "", "", ")", ""], 
                    ["", "math.factorial(", "", "", "", ")"], ["", "", "", "math.factorial(", "", ")"], 
                    ["((", "", ")", "", ")", ""], ["(", "(", "", "", "))", ""], ["", "((", "", "", ")", ")"], ["", "(", "", "(", "", "))"],   
                    ["math.sqrt((", "", ")", "", ")", ""], ["math.sqrt(", "(", "", "", "))", ""], ["", "math.sqrt((", "", "", ")", ")"], ["", "math.sqrt(", "", "(", "", "))"], 
                    ["(math.sqrt(", "", ")", "", ")", ""], ["(", "math.sqrt(", "", "", "))", ""], ["", "(math.sqrt(", "", "", ")", ")"], ["", "(", "", "math.sqrt(", "", "))"], 
                    ["math.factorial(math.sqrt(", "", ")", "", ")", ""], ["math.factorial(", "math.sqrt(", "", "", "))", ""], ["", "math.factorial(math.sqrt(", "", "", ")", ")"], ["", "math.factorial(", "", "math.sqrt(", "", "))"], 
                    ["math.sqrt(math.factorial(", "", ")", "", ")", ""], ["math.sqrt(", "math.factorial(", "", "", "))", ""], ["", "math.sqrt(math.factorial(", "", "", ")", ")"], ["", "math.sqrt(", "", "math.factorial(", "", "))"], 
                    ["(math.factorial(", "", ")", "", ")", ""], ["(", "math.factorial(", "", "", "))", ""], ["", "(math.factorial(", "", "", ")", ")"], ["", "(", "", "math.factorial(", "", "))"], ["math.factorial((", "", ")", "", ")", ""], 
                    ["math.factorial(", "(", "", "", "))", ""], ["", "math.factorial((", "", "", ")", ")"], ["", "math.factorial(", "", "(", "", "))"], ]

answer = []

for n in ALL_list_1:
    for m in ALL_list_2:
        for o in ALL_list_3:
            for p in ALL_list_4:
                if("kr" in n):
                    k = n.replace("kr","")
                    nn = "math.factorial(math.sqrt(" + k + ")))"
                elif("rk" in n):
                    k = n.replace("rk","")
                    nn = "math.sqrt(math.factorial(" + k + "))"
                elif("r" in n):
                    k = n.replace("r","")
                    nn = "math.sqrt(" + k + ")" 
                elif("k" in n):
                    k = n.replace("k","")
                    nn = "math.factorial(" + k + ")"
                else:
                    nn = n
                    
                if("kr" in m):
                    k = m.replace("kr","")
                    mm = "math.factorial(math.sqrt(" + k + "))"
                elif("rk" in m):
                    k = m.replace("rk","")
                    mm = "math.sqrt(math.factorial(" + k + "))"
                elif("r" in m):
                    k = m.replace("r","")
                    mm = "math.sqrt(" + k + ")" 
                elif("k" in m):
                    k = m.replace("k","")
                    mm = "math.factorial(" + k + ")"
                else:
                    mm = m
                    
                if("kr" in o):
                    k = o.replace("kr","")
                    oo = "math.factorial(math.sqrt(" + k + "))"
                elif("rk" in o):
                    k = o.replace("rk","")
                    oo = "math.sqrt(math.factorial(" + k + "))"
                elif("r" in o):
                    k = o.replace("r","")
                    oo = "math.sqrt(" + k + ")" 
                elif("k" in o):
                    k = o.replace("k","")
                    oo = "math.factorial(" + k + ")"
                else:
                    oo = o
                
                if("kr" in p):
                    k = p.replace("kr","")
                    pp = "math.factorial(math.sqrt(" + k + "))"
                elif("rk" in p):
                    k = p.replace("rk","")
                    pp = "math.sqrt(math.factorial(" + k + "))"
                elif("r" in p):
                    k = p.replace("r","")
                    pp = "math.sqrt(" + k + ")" 
                elif("k" in p):
                    k = p.replace("k","")
                    pp = "math.factorial(" + k + ")"
                else:
                    pp = p
                    
                symbol_pattern = itertools.combinations_with_replacement(symbol_list, 3)
                symbol_pattern_list = []
                for a in symbol_pattern:
                    x = itertools.permutations(a)
                    for b in x:
                        symbol_pattern_list.append(b)
                        
                symbol_pattern_list = set(symbol_pattern_list)
                    
                for q in symbol_pattern_list:
                    for r in parentheses_list:
                          
                        txt = str(r[0]) + nn + q[0] + str(r[1]) + mm + str(r[2]) + q[1] + str(r[3]) + oo + str(r[4]) + q[2] + pp + str(r[5])
                        formula = str( r[0]) + n + q[0] + str(r[1]) + m + str(r[2]) + q[1] + str(r[3]) + o + str(r[4]) + q[2] + p + str(r[5])

                        try:    
                            ans = eval(txt)
                            if("math.sqrt" in formula):
                                formula = formula.replace("math.sqrt", "√")
                            
                            if("math.factorial" in formula):
                                formula = formula.replace("math.factorial", "!")
                                
                            if("r" in formula):
                                formula = formula.replace("r", "√")
                            
                            if("k" in formula):
                                formula = formula.replace("k", "!")
                            
                            if(ans.is_integer()):
                                answer.append(ans)
                            
                        except:
                            pass

answer = sorted(set(answer))
print(answer)
