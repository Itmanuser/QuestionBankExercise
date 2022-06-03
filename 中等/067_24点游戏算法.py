"""
给出4个1-10的数字，通过加减乘除运算，得到数字为24就算胜利,除法指实数除法运算,运算符仅允许出现在两个数字之间,本题对数字选取顺序无要求
但每个数字仅允许使用一次，且需考虑括号运算此题允许数字重复，
如3 3 4 4为合法输入，此输入一共有两个3，但是每个数字只允许使用一次，则运算过程中两个3都被选取并进行对应的计算操作。
"""
import itertools
def func(a,b,c,d):
    rules = ['+',"-","*","/",'+',"-","*","/",'+',"-","*","/"]
    all_rules = itertools.permutations(rules,3)
    for x,y,z in all_rules:
        result = eval("((({}{}{}){}{}){}{})".format(a,x,b,y,c,z,d))
        if result == 24 or result == 24.0:
            return 'true'


if __name__ == '__main__':
    n = input().split()
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
        print("false")