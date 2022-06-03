"""
找出字符串中第一个只出现一次的字符
"""
while True:
    try:
        n = input()
        res = -1
        for i in n:
            if n.count(i) == 1:
                res = i
                break 
        print(res)
    except:
        break 