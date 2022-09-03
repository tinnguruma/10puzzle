###<<1回の総当たりで全部求めろってのもあるけどそれは今回なしで>>###

#ライブラリのインポート
import math
import itertools
import re
from traceback import format_exc

#入力を求めて変数に代入(n1)
n1 = input("1>>")
n2 = input("2>>")
n3 = input("3>>")
n4 = input("4>>")

#どっからどこまで(int型
st = int(input("START?>>"))
en = int(input("END?>>"))

#各数のそのまま(n1)、ルートをかけたもの(rn1)、　階乗したもの、(kn1)、どっちもしたもの順番あり(krn1,rkn1)いずれもstr型
ALL_list_1 = [n1, str("r" + n1), str("k" + n1), str("kr" + n1), str("rk" + n1)]
ALL_list_2 = [n2, str("r" + n2), str("k" + n2), str("kr" + n2), str("rk" + n2)]
ALL_list_3 = [n3, str("r" + n3), str("k" + n3), str("kr" + n3), str("rk" + n3)]
ALL_list_4 = [n4, str("r" + n4), str("k" + n4), str("kr" + n4), str("rk" + n4)]

#四則演算リスト
symbol_list = ["-", "+", "*", "/"]

#6つの括弧が配置される位置[(A+(B)+(C)+D)]のどこに括弧が入るかの全パターンリスト(それぞれにルート、階乗したものも全パターン)
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

#今はまだ役目なし
answer = []

#措定された範囲での実行
for l in range(st, en):
    
    #全てのやつ総当たり
    for n in ALL_list_1:
        for m in ALL_list_2:
            for o in ALL_list_3:
                for p in ALL_list_4:

                    #ここでさっきの(rn1)とかを変換する最初にやってもよかった
                    #最初の英語をとってそれぞれの数へ変形させる
                    #最後の式には残しておきたいから出た値はそれぞれnn,mm,oo,ppに代入
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
                        
                    #四則演算リストから3つを選ぶ(重複あり)
                    symbol_pattern = itertools.combinations_with_replacement(symbol_list, 3)
                    
                    #それで総当たり
                    for q in symbol_pattern:
                      
                        #かっこの配置で総当たり
                        for r in parentheses_list:
                              
                            #str型で式を書く
                            txt = str(r[0]) + nn + q[0] + str(r[1]) + mm + str(r[2]) + q[1] + str(r[3]) + oo + str(r[4]) + q[2] + pp + str(r[5])
                            formula = str( r[0]) + n + q[0] + str(r[1]) + m + str(r[2]) + q[1] + str(r[3]) + o + str(r[4]) + q[2] + p + str(r[5])
                            
                            #0で割れない処理があるのでtryで
                            try:
                                
                                #計算結果をansに代入(strで計算可能
                                ans = eval(txt)
                                
                                #最初のforの数字=現在のロールだったら
                                if (ans == l):
                                    
                                    #formuraという形で残しておいた式の関数を記号に直していく
                                    if("math.sqrt" in formula):
                                        formula = formula.replace("math.sqrt", "√")
                                    
                                    if("math.factorial" in formula):
                                        formula = formula.replace("math.factorial", "!")
                                        
                                    if("r" in formula):
                                        formula = formula.replace("r", "√")
                                    
                                    if("k" in formula):
                                        formula = formula.replace("k", "!")
                                    
                                    
                                    #結果の出力
                                    print(">>",l,"=",formula)
                                    
                                    #1個見つかったら総当たり中止->次の数字で
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
        #見つかんなかったらNO出力
        print(str(l) , "NO!")
