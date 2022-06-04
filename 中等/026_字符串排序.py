"""
编写一个程序，将输入字符串中的字符按如下规则排序。
规则 1 ：英文字母从 A 到 Z 排列，不区分大小写。
如，输入： Type 输出： epTy
规则 2 ：同一个英文字母的大小写同时存在时，按照输入顺序排列。
如，输入： BabA 输出： aABb
规则 3 ：非英文字母的其它字符保持原来的位置。
如，输入： By?e 输出： Be?y
"""

while True:
    try:
        n = input()
        new_str = ''
        for i in n:
            if i.isalpha():
                new_str += i 
        b = sorted(new_str,key=str.upper)
        res = ''
        index = 0
        for num in range(len(n)):
            if n[num].isalpha():
                res += b[index]
                index += 1
            else:
                res += n[num]
        print(res)
    except:
        break