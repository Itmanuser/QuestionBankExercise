"""
蛇形矩阵是由1开始的自然数依次排列成的一个矩阵上三角形。
例如，当输入5时，应该输出的三角形为：
1 3 6 10 15
2 5 9 14
4 8 13
7 12
11
"""

while True:
    try:
        n = int(input())
        for i in range(0,n):
            if i == 0:
                res = [((s+1)*(s+2)//2) for s in range(0,n)]
                print(" ".join(map(str,res)))
            else:
                res = [(n-1) for n in res[1:]]
                print(" ".join(map(str,res)))
    except:
        break 