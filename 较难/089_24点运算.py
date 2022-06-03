"""
计算24点是一种扑克牌益智游戏，随机抽出4张扑克牌，通过加(+)，减(-)，乘(*), 除(/)四种运算法则计算得到整数24，本问题中，扑克牌通过如下字符或者字符串表示，
其中，小写joker表示小王，大写JOKER表示大王：3 4 5 6 7 8 9 10 J Q K A 2 joker JOKER
本程序要求实现：输入4张牌，输出一个算式，算式的结果为24点。
"""

import itertools

card_dict = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}

def func(a,b,c,d):
    a1,b1,c1,d1 = card_dict[a],card_dict[b],card_dict[c],card_dict[d]
    rules = ['+',"-","*","/",'+',"-","*","/",'+',"-","*","/"]
    all_rules = itertools.permutations(rules,3)
    for x,y,z in all_rules:
        result = eval("((({}{}{}){}{}){}{})".format(a1,x,b1,y,c1,z,d1))
        if result == 24 or result == 24.0:
            return "{}{}{}{}{}{}{}".format(a,x,b,y,c,z,d)


if __name__ == '__main__':
    n = input().split()
    if "joker" in n or 'JOKER' in n:
        print("ERROR")
    else:
        res_list = []
        all_range = itertools.permutations(n,4)
        for one_range in all_range:
            a,b,c,d = one_range
            res = func(a,b,c,d)
            if res:
                res_list.append(res)
        if res_list:
            print(res_list[0])
        else:
            print("NONE")