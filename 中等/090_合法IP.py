"""
IPV4地址可以用一个32位无符号整数来表示，一般用点分方式来显示，点将IP地址分成4个部分，每个部分为8位，表示成一个无符号整数
（因此正号不需要出现），如10.137.17.1，是我们非常熟悉的IP地址，一个IP地址串中没有空格出现（因为要表示成一个32数字）。
现在需要你用程序来判断IP是否合法。
"""

while True:
    try:
        n = input().split(".")
        if len(n) != 4:
            print('NO')
        else:
            for i in n:
                if not i.isdigit() or (len(i)>1 and i[0] == "0") or int(i) > 255 or int(i) < 0:
                    print("NO")
                    break
            else:
                print("YES")
        
    except:
        break 