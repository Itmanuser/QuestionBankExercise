"""
请计算n*m的棋盘格子（n为横向的格子数，m为竖向的格子数）从棋盘左上角出发沿着边缘线从左上角走到右下角，总共有多少种走法，
要求不能走回头路，即：只能往右和往下走，不能往左和往上走。
"""

def func(x,y):
    if x < 0 or y < 0:
        return 0
    elif x == 0 or y == 0:
        return 1
    else:
        return func(x-1, y) + func(x, y-1)

while True:
    try:
        a,b = map(int,input().split())
        c = func(a, b)
        print(c)
    except:
        break