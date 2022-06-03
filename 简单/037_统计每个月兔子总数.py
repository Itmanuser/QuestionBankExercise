"""
有一种兔子，从出生后第3个月起每个月都生一只兔子，小兔子长到第三个月后每个月又生一只兔子。
例子：假设一只兔子第3个月出生，那么它第5个月开始会每个月生一只兔子。
一月的时候有一只兔子，假如兔子都不死，问第n个月的兔子总数为多少？
"""
def f(n):
    if n <= 2:
        return 1
    else:
        return f(n-1)+f(n-2)
     
while True:
    try:
        n=int(input())
        print(f(n))
    except:
        break